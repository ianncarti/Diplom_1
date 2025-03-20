import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize('price', [1.15, 0, -1, 1])
    def test_ingredient_get_price(self, price):
        new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Сус", price)

        assert new_ingredient.get_price() == price

    @pytest.mark.parametrize('name', ["Мегасус", "Supersus"])
    def test_ingredient_get_name(self, name):
        new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 1)

        assert new_ingredient.get_name() == name

    @pytest.mark.parametrize('ingr_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_ingredient_get_type(self, ingr_type):
        new_ingredient = Ingredient(ingr_type, "Сус", 1)

        assert new_ingredient.get_type() == ingr_type
