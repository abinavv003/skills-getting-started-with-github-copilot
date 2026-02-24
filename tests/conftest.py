from pathlib import Path
import sys
from copy import deepcopy
import pytest
from fastapi.testclient import TestClient

# Make sure repo root is importable so we can import src.app
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

import src.app as app_module

app = app_module.app
_initial_activities = deepcopy(app_module.activities)


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def reset_activities():
    # Restore in-memory activities before each test
    app_module.activities.clear()
    app_module.activities.update(deepcopy(_initial_activities))
    yield
