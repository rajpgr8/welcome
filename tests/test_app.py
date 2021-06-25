import pytest

def test_1stTest_1():
  print("1stTest-1")
  assert 1 == 1
  
@pytest.mark.smoke  
def test_1stTest_2():
  print("1stTest-2")
  assert 1 == 1
    
def test_1stTest_3():
  print("1stTest-3")
  assert 1 == 1

@pytest.mark.skip  
def test_1stTest_4():
  print("1stTest-4")
  assert 1 == 1
