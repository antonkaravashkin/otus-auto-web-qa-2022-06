from src.Rectangle import Rectangle
from data.geom_data import BAG_RECTANGLE, RECTANGLE_NAME, EXPECTED_RECTANGLE_AREA, EXPECTD_RECTANGLE_PERIMETER
import pytest


def test_impossible_triangle_creation():
    """
    Тест создания не правильного прямоугольника
    """
    with pytest.raises(ValueError):
        Rectangle(*BAG_RECTANGLE)


def test_triangle_creation(rectangle_creation):
    """
    Тест проверяет успешное создание экземпляра класса Rectangle
    """
    assert type(rectangle_creation) == Rectangle


def test_triangle_name(rectangle_creation):
    """
    Тест проверяет атрибут name
    """
    assert rectangle_creation.name == RECTANGLE_NAME, \
        f"Ожидалось имя {RECTANGLE_NAME}, пришло {rectangle_creation.name}"


def test_triangle_add_area(rectangle_creation, square_creation):
    added_area = rectangle_creation.add_area(square_creation)
    assert added_area == square_creation.add_area(rectangle_creation), "Передена не фигура"


def test_triangle_wrong_figure(rectangle_creation):
    with pytest.raises(ValueError):
        rectangle_creation.add_area(10)


def test_triangle_area(rectangle_creation):
    assert rectangle_creation.area == EXPECTED_RECTANGLE_AREA, \
        f"Площади не совпадают, ожидалось {EXPECTED_RECTANGLE_AREA}"


def test_triangle_perimeter(rectangle_creation):
    assert rectangle_creation.perimeter == EXPECTD_RECTANGLE_PERIMETER, \
        f"Периметр не совпадает, ожидался {EXPECTD_RECTANGLE_PERIMETER}"
