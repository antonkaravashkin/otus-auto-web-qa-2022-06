from src.Square import Square
from data.geom_data import SQUARE_NAME, BAD_SQUARE, EXPECTED_SQUARE_AREA, EXPECTD_SQUARE_PERIMETER
import pytest


def test_impossible_square_creation():
    """
    Тест создания квадрата с кривой стороной
    """
    with pytest.raises(ValueError):
        Square(BAD_SQUARE)


def test_square_creation(square_creation):
    """
    Тест проверяет успешное создание экземпляра класса Square
    """
    assert type(square_creation) == Square


def test_square_name(square_creation):
    """
    Тест проверяет атрибут name
    """
    assert square_creation.name == SQUARE_NAME, \
        f"Ожидалось имя {SQUARE_NAME}, пришло {square_creation.name}"


def test_square_add_area(triangle_creation, square_creation):
    added_area = triangle_creation.add_area(square_creation)
    assert added_area == square_creation.add_area(triangle_creation), "Передена не фигура"


def test_square_wrong_figure(square_creation):
    with pytest.raises(ValueError):
        square_creation.add_area(10)


def test_square_area(square_creation):
    assert square_creation.area == EXPECTED_SQUARE_AREA, f"Площади не совпадают, ожидалось {EXPECTED_SQUARE_AREA}"


def test_square_perimeter(square_creation):
    assert square_creation.perimeter == EXPECTD_SQUARE_PERIMETER, \
        f"Периметр не совпадает, ожидался {EXPECTD_SQUARE_PERIMETER}"
