import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
  def test_fixtureDemo_1(self):
    print("test_fixtureDemo_1")
    
  def test_fixtureDemo_2(self):
    print("test_fixtureDemo_2")

@pytest.mark.usefixtures("loadSomeData")
class TestExample_2:
  def test_fixtureDemo_3(self, loadSomeData):
    print("test_fixtureDemo_2")
    print(loadSomeData)
  
