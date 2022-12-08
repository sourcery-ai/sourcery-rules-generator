import os
from pathlib import Path
import pytest


@pytest.fixture
def yaml_rules_only_api_imports_core():
    return Path(
        os.path.dirname(__file__),
        "fixtures/dependency-rules/core-imported-only-by-api.yaml",
    ).read_text()
