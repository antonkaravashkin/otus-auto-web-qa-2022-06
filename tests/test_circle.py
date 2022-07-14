from src.Circle import Circle
from data.geom_data import BAD_CIRCLE, CIRCLE_NAME, EXPECTED_CIRCLE_AREA, EXPECTD_CIRCLE_PERIMETER
import pytest


def test_impossible_circle_creation():
    """
    Тест создания не правильного круга
    """
    with pytest.raises(ValueError):
        Circle(BAD_CIRCLE)


def test_circle_creation(circle_creation):
    """
    Тест проверяет успешное создание экземпляра класса Circle
    """
    assert type(circle_creation) == Circle


def test_circle_name(circle_creation):
    """
    Тест проверяет атрибут name
    """
    assert circle_creation.name == CIRCLE_NAME, \
        f"Ожидалось имя {CIRCLE_NAME}, пришло {circle_creation.name}"


def test_circle_add_area(circle_creation, square_creation):
    added_area = circle_creation.add_area(square_creation)
    assert added_area == square_creation.add_area(circle_creation), "Передена не фигура"


def test_circle_wrong_figure(circle_creation):
    with pytest.raises(ValueError):
        circle_creation.add_area(10)


def test_circlee_area(circle_creation):
    assert circle_creation.area == EXPECTED_CIRCLE_AREA, f"Площади не совпадают, ожидалось {EXPECTED_CIRCLE_AREA}"


def test_circle_perimeter(circle_creation):
    assert circle_creation.perimeter == EXPECTD_CIRCLE_PERIMETER, \
        f"Периметр не совпадает, ожидался {EXPECTD_CIRCLE_PERIMETER}"
