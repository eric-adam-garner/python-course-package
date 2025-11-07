import subprocess
from pathlib import Path

from tests.fixtures.project_dir import project_dir


def test_linting(project_dir: Path):
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)
    