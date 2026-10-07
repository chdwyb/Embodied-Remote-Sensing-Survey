"""Validate the public catalogue, links, indexes, and exact repository file set."""

from pathlib import Path
from urllib.parse import unquote, urlparse
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_FILES = {
    ".gitignore", ".gitattributes", "README.md", "README_zh-CN.md", "CONTRIBUTING.md",
    "data/literature.json", "data/references.bib", "data/resources.json",
    "docs/papers.md", "docs/papers-by-year.md", "docs/datasets.md",
    "scripts/generate_catalogue.py", "scripts/validate_repository.py", "scripts/LICENSE",
}
REFERENCE_FIELDS = {
    "citation_key", "title", "authors_bibtex", "publication_year", "venue_full", "venue_display",
    "display_name", "primary_category", "categories", "record_role", "bibtex_type", "bibtex_fields",
    "links", "paper_url", "code_url", "project_urls",
}
BIB_FIELDS = {
    "author", "booktitle", "doi", "howpublished", "journal", "number", "pages", "publisher",
    "series", "sourceurl", "title", "url", "volume", "year",
}
RESOURCE_FIELDS = {"name", "primary_source", "modalities", "supported_task"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_json(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8-sig"))


def valid_url(value):
    require(isinstance(value, str), "URL must be a string")
    parsed = urlparse(value)
    require(parsed.scheme in {"http", "https"} and parsed.netloc and "\\" not in value
            and not any(character.isspace() for character in value), f"Invalid public URL: {value}")


def parse_bibliography(contents):
    """Read the catalogue's braced-value BibTeX without external dependencies."""
    position = 0
    entries = {}
    while position < len(contents):
        if contents[position].isspace():
            position += 1
            continue
        entry = re.match(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", contents[position:])
        require(entry is not None, f"Unexpected BibTeX text at offset {position}")
        kind, key = entry.groups()
        require(key not in entries, f"Duplicate bibliography key: {key}")
        position += entry.end()
        fields = {}
        while True:
            while position < len(contents) and (contents[position].isspace() or contents[position] == ","):
                position += 1
            require(position < len(contents), f"Unclosed bibliography entry: {key}")
            if contents[position] == "}":
                position += 1
                break
            field = re.match(r"(\w+)\s*=\s*\{", contents[position:])
            require(field is not None, f"Invalid braced bibliography field in {key}")
            name = field.group(1).casefold()
            require(name not in fields, f"Duplicate bibliography field: {key}/{name}")
            position += field.end()
            start = position
            depth = 1
            while position < len(contents) and depth:
                character = contents[position]
                if character == "\\":
                    position += 2
                    continue
                if character == "{":
                    depth += 1
                elif character == "}":
                    depth -= 1
                position += 1
            require(depth == 0, f"Unclosed bibliography field: {key}/{name}")
            fields[name] = contents[start:position - 1]
        entries[key] = (kind.casefold(), fields)
    return entries


def heading_ids(contents):
    ids = set(re.findall(r'<a\s+id="([^"]+)"', contents))
    counts = {}
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*$", contents):
        slug = re.sub(r"[^\w -]", "", heading.casefold()).replace(" ", "-")
        number = counts.get(slug, 0)
        ids.add(slug if number == 0 else f"{slug}-{number}")
        counts[slug] = number + 1
    return ids


def validate_markdown_links():
    for path in ROOT.rglob("*.md"):
        if ".git" in path.relative_to(ROOT).parts:
            continue
        contents = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        require(not re.search(r"!\[[^\]]*\]\(", contents), f"Image embed in {path.relative_to(ROOT)}")
        require(not re.search(r"<\s*(?:img|svg|iframe)\b", contents, flags=re.I), f"Visual embed in {path.relative_to(ROOT)}")
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", contents):
            parsed = urlparse(target)
            if parsed.scheme:
                valid_url(target)
                continue
            filename, separator, anchor = target.partition("#")
            destination = (path.parent / unquote(filename)).resolve() if filename else path
            require(destination == ROOT or ROOT in destination.parents, f"Link leaves repository: {target}")
            require(destination.exists(), f"Missing local link: {path.relative_to(ROOT)} -> {target}")
            if separator and anchor and destination.is_file() and destination.suffix == ".md":
                require(unquote(anchor) in heading_ids(destination.read_text(encoding="utf-8")),
                        f"Missing heading link: {path.relative_to(ROOT)} -> {target}")


def main():
    actual = {path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*")
              if path.is_file() and path.relative_to(ROOT).parts[0] != ".git"}
    require(actual == ALLOWED_FILES,
            f"Repository file set differs: extra={sorted(actual - ALLOWED_FILES)}, missing={sorted(ALLOWED_FILES - actual)}")
    catalogue = load_json("data/literature.json")
    require(set(catalogue) == {"categories", "references"}, "Unexpected catalogue metadata")
    records = catalogue["references"]
    categories = catalogue["categories"]
    require(isinstance(categories, dict) and set(categories) == {
        "C1", "C2", "C3", "C4", "C5", "resources", "background", "related_surveys"
    }, "Unexpected categories")
    require(isinstance(records, list) and records, "Catalogue must contain public bibliographic entries")
    keys = [record["citation_key"] for record in records]
    require(len(keys) == len(set(keys)), "Duplicate catalogue keys")
    bibliography = parse_bibliography((ROOT / "data/references.bib").read_text(encoding="utf-8-sig"))
    require(set(bibliography) == set(keys), "JSON and BibTeX keys differ")
    for record in records:
        key = record["citation_key"]
        require(set(record) == REFERENCE_FIELDS, f"Unexpected catalogue fields: {key}")
        require(re.fullmatch(r"[A-Za-z0-9_-]+", key) and not re.match(r"(?:v\d+|exp)_", key, flags=re.I),
                f"Invalid key: {key}")
        require(record["title"] and "\ufffd" not in record["title"], f"Invalid title: {key}")
        require(isinstance(record["publication_year"], int) and 1800 <= record["publication_year"] <= 2100,
                f"Invalid publication year: {key}")
        require(record["primary_category"] in categories and set(record["categories"]) <= set(categories)
                and record["primary_category"] in record["categories"], f"Invalid classification: {key}")
        require(set(record["bibtex_fields"]) <= BIB_FIELDS, f"Unexpected bibliographic fields: {key}")
        require(bibliography[key] == (record["bibtex_type"].casefold(), record["bibtex_fields"]),
                f"JSON/BibTeX field mismatch: {key}")
        require(record["authors_bibtex"] == record["bibtex_fields"].get("author", ""), f"Author mismatch: {key}")
        require(str(record["publication_year"]) == record["bibtex_fields"].get("year"), f"Year mismatch: {key}")
        require(isinstance(record["links"], list) and isinstance(record["project_urls"], list), f"Invalid link fields: {key}")
        for item in record["links"]:
            require(set(item) == {"kind", "url"} and item["kind"] in {"paper", "code", "project"}, f"Invalid link kind: {key}")
            valid_url(item["url"])
        require(len({(item["kind"], item["url"]) for item in record["links"]}) == len(record["links"]),
                f"Duplicate links: {key}")
        for kind in ("paper", "code"):
            primary = next((item["url"] for item in record["links"] if item["kind"] == kind), None)
            require((record[f"{kind}_url"] or None) == primary, f"Primary link mismatch: {key}/{kind}")
        require(record["project_urls"] == [item["url"] for item in record["links"] if item["kind"] == "project"],
                f"Project link mismatch: {key}")

    resources = load_json("data/resources.json")
    require(set(resources) == {"resources"} and isinstance(resources["resources"], list) and resources["resources"],
            "Unexpected or empty resource directory")
    require(len({record["name"] for record in resources["resources"]}) == len(resources["resources"]), "Duplicate resource names")
    for record in resources["resources"]:
        require(set(record) == RESOURCE_FIELDS and all(isinstance(value, str) and value for value in record.values()),
                "Unexpected resource fields or empty description")
        valid_url(record["primary_source"])
    validate_markdown_links()
    subprocess.run([sys.executable, str(ROOT / "scripts/generate_catalogue.py"), "--check"], check=True)
    print(f"PASS: exact public file set; {len(records)} matching bibliography records; "
          f"{len(resources['resources'])} resources; valid links; current paper indexes.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        raise SystemExit(f"FAIL: {error}") from error
