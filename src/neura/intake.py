from __future__ import annotations

import hashlib
from pathlib import Path


def sha256(path: str | Path, chunk_size: int = 1024 * 1024) -> str:
    """Return the SHA-256 checksum for a file without loading it all into memory."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def inventory(root: str | Path) -> list[dict[str, object]]:
    """Return a simple recursive file inventory for dataset intake."""
    base = Path(root)
    rows: list[dict[str, object]] = []
    if not base.exists():
        return rows

    for path in sorted(p for p in base.rglob("*") if p.is_file()):
        stat = path.stat()
        rows.append(
            {
                "path": str(path.relative_to(base)),
                "bytes": stat.st_size,
                "suffix": path.suffix.lower(),
            }
        )
    return rows
