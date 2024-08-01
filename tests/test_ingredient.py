import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:

    def test_get_price_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Биокотлета из марсианской Магнолии', 424.90)
        assert ingredient.get_price() == 424.90

    def test_get_name_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
        assert ingredient.get_name() == 'Соус Spicy-X'

    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Хрустящие минеральные кольца', 300, 'FILLING']
        ]
    )
    def test_get_type_correct_type(self, type, name, price, expected_ingredient):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_ingredient
