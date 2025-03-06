import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from tests.conftest import burger
from unittest.mock import Mock


class TestBurger:

    def test_burger_set_buns(self, burger):
        mock_bun = Mock()
        mock_bun.configure_mock(name='булочька', price=10)
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @pytest.mark.parametrize('ingr_type', [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE])
    def test_burger_add_ingredient(self, burger, ingr_type):
        mock_ingr = Mock()
        mock_ingr.configure_mock(type=ingr_type, name='моковый ингридиент', price=2.2)
        burger.add_ingredient(mock_ingr)
        assert mock_ingr in burger.ingredients

    @pytest.mark.parametrize('ingr_type', [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE])
    def test_burger_remove_ingredient(self, burger, ingr_type):
        mock_ingr = Mock()
        mock_ingr.configure_mock(type=ingr_type, name='моковый ингридиент', price=2.2)
        burger.add_ingredient(mock_ingr)
        burger.remove_ingredient(0)
        assert mock_ingr not in burger.ingredients

    def test_burger_move_ingredient(self, burger):
        mock_ingr_1 = Mock()
        mock_ingr_2 = Mock()
        mock_ingr_1.configure_mock(type='Соус', name='моковый ингридиент 1', price=2.2)
        mock_ingr_2.configure_mock(type='Филлер', name='моковый ингридиент 2', price=2)

        burger.add_ingredient(mock_ingr_1)
        burger.add_ingredient(mock_ingr_2)
        burger.move_ingredient(1, 0)  #второй ингредиент поменяли местами с первым

        assert burger.ingredients[0] == mock_ingr_2

    def test_burger_get_price(self, burger):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 10
        mock_ingr = Mock()
        mock_ingr.get_price.return_value = 2.2
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingr)
        assert burger.get_price() == 22.2

    @pytest.mark.parametrize('ingr_type', [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE])
    def test_burger_get_receipt(self, burger, ingr_type):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'булочька'
        mock_bun.get_price.return_value = 10
        burger.set_buns(mock_bun)

        mock_ingr = Mock()
        mock_ingr.get_name.return_value = 'моковый ингридиент'
        mock_ingr.get_price.return_value = 2.2
        mock_ingr.get_type.return_value = ingr_type
        burger.add_ingredient(mock_ingr)

        receipt = burger.get_receipt()

        assert mock_bun.get_name() in receipt
        assert mock_ingr.get_type().lower() in receipt
        assert mock_ingr.get_name() in receipt
        assert str(burger.get_price()) in receipt
