import pytest

@pytest.fixture()
def setup():
  print("setup: ***setup() will be executed before any other tests (dependent on this fixture) run***")

