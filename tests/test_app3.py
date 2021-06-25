import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
  def test_fixtureDemo_1(self):
    print("test_fixtureDemo_1")
    
  def test_fixtureDemo_2(self):
    print("test_fixtureDemo_2")

@pytest.mark.usefixtures("loadSomeData")
class TestExample_LoadData:
  def test_loadData_check(self, loadSomeData):
    print("test_loadData_check")
    print(loadSomeData)
  

  
@pytest.mark.usefixtures("parameterizedOption")
class TestExample_parameterizedOptionCheck:
  def test_parameterizedOption_check(self, parameterizedOption):
    print("test_parameterizedOption_check")
    print(parameterizedOption)
