from neura.intake import inventory
from neura.paths import project_root


def test_project_root_exists():
    assert project_root().exists()


def test_inventory_missing_directory_is_empty(tmp_path):
    assert inventory(tmp_path / "missing") == []
