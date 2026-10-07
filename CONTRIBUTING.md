# Contributing

Please include a public paper, publisher page or author project page when proposing an addition. Provide the title, authors, publication year, venue, relevant topic and author-maintained code link when available.

## Updating the directory

1. Add or correct the record in `data/literature.json`. Keep citation keys unique and use the categories defined in that file.
2. Update the matching entry in `data/references.bib`.
3. For a dataset or platform, update `data/resources.json` and `docs/datasets.md` with its source, modalities and supported task.
4. Regenerate the paper indexes and validate the repository:

```sh
python scripts/generate_catalogue.py
python scripts/validate_repository.py
```

The utilities use the Python standard library. Paper, code and project links should point to primary sources. When reporting a correction, identify the entry and link to evidence supporting the change.

The [MIT license](scripts/LICENSE) applies to the utilities in `scripts/`. External publications, software and datasets retain their original licenses.
