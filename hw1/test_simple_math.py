from simple_math import SimpleMath
import pytest

@pytest.fixture
def simple_math():
    return SimpleMath()


def test_square_positive_numbers(simple_math):
    assert simple_math.square(2) == 4


def test_square_negative_numbers(simple_math):
    assert simple_math.square(-4) == 16


def test_square_floats(simple_math):
    assert simple_math.square(2.5) == 6.25


def test_square_by_zero(simple_math):
    assert simple_math.square(0) == 0


def test_cube_positive_numbers(simple_math):
    assert simple_math.cube(3) == 27


def test_cube__negative_numbers(simple_math):
    assert simple_math.cube(-3) == -27


def test_cube_floats(simple_math):
    assert simple_math.cube(2.1) == 9.261


def test_cube_by_zero(simple_math):
        assert simple_math.cube(0) == 0

