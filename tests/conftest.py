import pytest

@pytest.fixture()
def setup():
  print("setup: ***should be exceuted this setup() before other fixture test run***")

