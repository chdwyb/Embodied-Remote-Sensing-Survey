"""Generate public paper indexes from the bibliographic catalogue."""

from pathlib import Path
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def cell(value):
    return str(value or "—").replace("|", "\\|").replace("\n", " ")


def link(url, label):
    return f"[{label}]({url})" if url else ""


def links(record):
    entries = [link(item["url"], item["kind"].capitalize()) for item in record["links"]]
    return " · ".join(dict.fromkeys(item for item in entries if item)) or "—"


def sorted_records(records):
    return sorted(records, key=lambda record: (-int(record["publication_year"]), record["title"].casefold()))


def table(records):
    rows = ["| Paper | Venue / year | Category | Links |", "| --- | --- | --- | --- |"]
    for record in sorted_records(records):
        rows.append("| " + " | ".join([
            f'<a id="{record["citation_key"]}"></a>{cell(record["title"])}',
            cell(record["venue_display"]),
            cell(record["primary_category"]),
            links(record),
        ]) + " |")
    return "\n".join(rows)


def slug(text):
    return re.sub(r"[^\w -]", "", text.casefold()).replace(" ", "-")


def generated_files():
    catalogue = json.loads((ROOT / "data/literature.json").read_text(encoding="utf-8"))
    records = catalogue["references"]
    introduction = (
        "Public literature on geospatial grounding, aerial navigation, adaptive sensing, predictive models, "
        "and cooperative observation, with related datasets and background work. "
        "Categories overlap; each entry's primary category provides a navigation aid.\n\n"
        "Each entry links to its available public paper, code and project sources.\n\n"
        "[Repository overview](../README.md) · [Datasets](datasets.md) · "
        "[Bibliography](../data/references.bib) · [Machine-readable catalogue](../data/literature.json)\n"
    )
    category_index = ["# Papers by category", "", introduction, "## Navigation", ""]
    for category, title in catalogue["categories"].items():
        category_index.append(f"- [{category}: {title}](#{slug(category + ': ' + title)})")
    for category, title in catalogue["categories"].items():
        subset = [record for record in records if record["primary_category"] == category]
        category_index.extend(["", f"## {category}: {title}", "", table(subset)])
    year_index = ["# Papers by publication year", "", introduction, "[Category index](papers.md)", "", "## Navigation", ""]
    years = sorted({int(record["publication_year"]) for record in records}, reverse=True)
    for year in years:
        year_index.append(f"- [{year}](#{year})")
    for year in years:
        subset = [record for record in records if int(record["publication_year"]) == year]
        year_index.extend(["", f"## {year}", "", table(subset)])
    return {
        "docs/papers.md": "\n".join(category_index) + "\n",
        "docs/papers-by-year.md": "\n".join(year_index) + "\n",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check indexes without changing files")
    args = parser.parse_args()
    stale = []
    for relative, content in generated_files().items():
        path = ROOT / relative
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    if stale:
        raise SystemExit("Regenerate paper indexes: " + ", ".join(stale))
    print("Paper indexes are current." if args.check else "Generated category and publication-year paper indexes.")


if __name__ == "__main__":
    main()
