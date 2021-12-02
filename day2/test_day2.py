import pytest
from day2 import load_data, calc_final, Direction, CalcB

def test_load_data():
    data = load_data('test_data.txt')
    assert data[0] == Direction("forward", 5)

def test_calc_final():
    data = load_data('test_data.txt')
    final = calc_final(data)
    assert final == 150

def test_calc_b():
    data = load_data('test_data.txt')
    final = CalcB(parsed_input=data).calc_final()
    assert final == 900