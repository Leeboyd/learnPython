import pytest

@pytest.fixture
def input_value():
    return 100

@pytest.mark.great
def test_greater(input_value):
    num = input_value
    assert num > 100

@pytest.mark.great
def test_greater_equal(input_value):
    num = input_value
    assert num >= 100

@pytest.mark.others
def test_less(input_value):
   num = input_value
   assert num < 200