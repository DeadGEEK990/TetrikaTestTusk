import pytest
from .solution import strict


@strict
def string_func(a: str, b: str) -> str:
    return f'{a}, {b}'


@strict
def float_func(a: float, b: float) -> float:
    return a+b


@strict
def bool_func(a: bool, b: bool) -> bool:
    return a==b


@strict
def int_func(a: int, b: int) -> int:
    return a+b


# Тесты


def test_string_func_whit_correct_types():
    assert string_func('Hello','World!') == 'Hello, World!'


def test_string_func_whit_incorrect_types():
    with pytest.raises(TypeError):
        string_func('Hello',True)


def test_float_func_whit_correct_types():
    assert float_func(2.4, 3.1) == 5.5


def test_float_func_whit_incorrect_types():
    with pytest.raises(TypeError):
        float_func(1, 2.2)


def test_bool_func_whit_correct_types():
    assert bool_func(True, True) == True


def test_bool_func_whit_incorrect_types():
    with pytest.raises(TypeError):
        bool_func(True, 1)


def test_int_func_whit_correct_types():
    assert int_func(2, 1) == 3


def test_int_func_whit_incorrect_types():
    with pytest.raises(TypeError):
        int_func(1, 2.2)