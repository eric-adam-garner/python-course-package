import shutil
import subprocess
from pathlib import Path
from typing import Generator

import pytest

from tests.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Generator[Path, None, None]:
    
    template_values = {"repo_name": "test-repo"}
    generated_repo_dir: Path = generate_project(template_values)
    initialize_git_repo(generated_repo_dir)
    subprocess.run(["make", "lint-ci"], cwd=generated_repo_dir, check=False)
    yield generated_repo_dir
    shutil.rmtree(generated_repo_dir)