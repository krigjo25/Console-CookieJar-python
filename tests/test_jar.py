#   CookieJar test suite.
import pytest
from app import Jar


def test_Constructor():

  jar = Jar()

  # Testing the default capacity
  assert jar.capacity == 12
  
  # Testing the custom capacity
  jar.capacity = 1
  assert jar.capacity == 1

  jar.capacity = 13

  assert jar.capacity == 13

  jar.size = ""
  assert jar.size == "zero cookies"

  return

def test_Deposit():

  jar = Jar()

  # Deposits one cookie
  jar.deposit(2)
  
  assert jar.size == "🍪🍪"

  jar.deposit(10)
  assert jar.size == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

  return

def test_withdraw():

  jar = Jar()

  jar.deposit(10)
  jar.withdraw(1)

  assert jar.size == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_ValueError():

  jar = Jar()

  #   Testing ValueError for the Constructor
  with pytest.raises(ValueError):
    jar.capacity = -1

  with pytest.raises(ValueError):
    jar.deposit(13)

  with pytest.raises(ValueError):
    jar.deposit(2)
    jar.withdraw(3)

  return
