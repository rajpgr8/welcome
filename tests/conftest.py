import pytest

@pytest.fixture()
def setup():
  print("setup: ***setup() will be executed before any other tests (dependent on this fixture) run***")

@pytest.fixture()
def loadSomeData():
  print("loadSomeData: ***loadSomeData()***")
  return ["Joe", 3, 700]
