from __future__ import annotations

import os
from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def data_dir() -> Path:
    configured = os.getenv("NEURA_DATA_DIR")
    return Path(configured).expanduser().resolve() if configured else project_root() / "data"


def output_dir() -> Path:
    configured = os.getenv("NEURA_OUTPUT_DIR")
    return Path(configured).expanduser().resolve() if configured else project_root() / "outputs"
