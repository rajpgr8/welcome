import pytest
import logging

class BaseLogger:
  def getLogger(self):
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('mylog.log')
    formater = logging.Formatter(" %(asctime)s :%(levelname)s :%s(name)s :%s(message)s")
    fileHandler.setFormatter(formater)
    
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
    return logger

@pytest.mark.usefixtures("setup")
class TestExample(BaseLogger):
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
