# Data directory

This directory is intentionally excluded from Git except for placeholders and this file.

- `raw/` — immutable source data received from a provider.
- `processed/` — cleaned or transformed intermediate files.
- `derived/` — features, summary tables and other reproducible derivatives.

## Rule

Do not commit FinalSpark recordings or any other third-party research dataset unless redistribution is explicitly permitted in writing.

Keep the original files unchanged in `raw/`. Any transformations should create new files in `processed/` or `derived/`.
