from pathlib import Path


def test_generate_project(project_dir: Path):
    assert project_dir.exists()
