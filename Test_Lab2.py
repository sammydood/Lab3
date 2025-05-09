import pytest
from lab2_submodule.lab2 import Lab2

def test_find_min_max_normal():
    temperatures = [22.5,24,19.8, 25.3, 21]
    assert Lab2.find_min_max(temperatures) == [19.8,25.3]

def test_find_min_max_sam_values():
    temperatures = [20,20,20]
    assert Lab2.find_min_max(temperatures) == [20,20]

def test_calc_average_normal():
    temperatures = [22.5, 24, 19.5]
    assert Lab2.calc_average(temperatures) == pytest.approx(22.0,0.01)

def test_calc_average_single_value():
    temperatures = [30]
    assert Lab2.calc_average(temperatures) == 30

def test_calc_median_odd():
    temperatures = [22.5,24,19.5]
    assert Lab2.calc_median_temperature(temperatures) == 22.5

def test_calc_median_even():
    temperatures = [22.5, 24, 19.5, 21]
    assert Lab2.calc_median_temperature(temperatures) == pytest.approx((21+22.5)/2,0.01)

def test_calc_median_sorted():
    temperatures = [19.5, 21, 22.5, 24]
    assert Lab2.calc_median_temperature(temperatures) == pytest.approx((21+22.5)/2,0.01)