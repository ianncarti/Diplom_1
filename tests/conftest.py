import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database


#Создаёт объект класса Bun
@pytest.fixture
def default_bun():
    bun = Bun('булобчка', 10)
    return bun

#Создаёт объект класса Burger
@pytest.fixture
def burger():
    burger = Burger()
    return burger

#Создаёт объект класса Database
@pytest.fixture
def database():
    db = Database()
    return db
