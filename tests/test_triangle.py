from src.Triangle import Triangle
from data.geom_data import BAD_TRIANGLE, TRIANGLE_NAME, EXPECTED_TRIANGLE_AREA, EXPECTD_TRIANGLE_PERIMETER
import pytest


def test_impossible_triangle_creation():
    """
    Тест создания треугольника без стороны
    """
    with pytest.raises(ValueError):
        Triangle(*BAD_TRIANGLE)


def test_triangle_creation(triangle_creation):
    """
    Тест проверяет успешное создание экземпляра класса Triangle
    """
    assert type(triangle_creation) == Triangle


def test_triangle_name(triangle_creation):
    """
    Тест проверяет атрибут name
    """
    assert triangle_creation.name == TRIANGLE_NAME, \
        f"Ожидалось имя {TRIANGLE_NAME}, пришло {triangle_creation.name}"


def test_triangle_add_area(triangle_creation, square_creation):
    added_area = triangle_creation.add_area(square_creation)
    assert added_area == square_creation.add_area(triangle_creation), "Передена не фигура"


def test_triangle_wrong_figure(triangle_creation):
    with pytest.raises(ValueError):
        triangle_creation.add_area(10)


def test_triangle_area(triangle_creation):
    assert triangle_creation.area == EXPECTED_TRIANGLE_AREA, f"Площади не совпадают, ожидалось {EXPECTED_TRIANGLE_AREA}"


def test_triangle_perimeter(triangle_creation):
    assert triangle_creation.perimeter == EXPECTD_TRIANGLE_PERIMETER, \
        f"Периметр не совпадает, ожидался {EXPECTD_TRIANGLE_PERIMETER}"
