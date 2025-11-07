import shutil
from pathlib import Path
from typing import Generator

import pytest

from tests.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Generator[Path, None, None]:
    
    print("Setup")
    template_values = {"repo_name": "test-repo"}
    generated_repo_dir: Path = generate_project(template_values)
    initialize_git_repo(generated_repo_dir)
    yield generated_repo_dir
    
    print("Teardown")
    shutil.rmtree(generated_repo_dir)