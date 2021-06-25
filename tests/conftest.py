import pytest

@pytest.fixture()
def setup():
  print("setup: should be exceuted before other fixture test run")

