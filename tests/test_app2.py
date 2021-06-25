  
import pytest

def test_2ndTest_1():
  print("2ndTest-1")
  assert 1 == 2  # will fail
    
def test_2ndTest_2(setup):
  print("1stTest-2")
  assert 1 == 1
  
def test_2ndTest_3():
  print("1stTest-3")
  assert 1 == 1
