import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
  def test_fixtureDemo_1(self):
    print("test_fixtureDemo_1")
    
  def test_fixtureDemo_2(self):
    print("test_fixtureDemo_2")
  
