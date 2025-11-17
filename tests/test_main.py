from simple_calculator.main import SimpleCalculator
import pytest

def test_add_two_numbers():
    numbers = range(100)
    calculator = SimpleCalculator()

    result = calculator.add(*numbers)
    assert result==4950

def test_subtract_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.sub(10,3)
    assert result == 7

def test_mul_two_numbers():
    numbers = range(1,10)
    calculator = SimpleCalculator()

    result = calculator.mul(*numbers)
    assert result == 362880

def test_div_two_numbers_float():
    calculator = SimpleCalculator()

    result = calculator.div(13, 2)
    assert result == 6.5

def test_div_by_zero_returns_inf():
    calculator = SimpleCalculator()

    result = calculator.div(5, 0)
    assert result == float('inf')

def test_mul_by_zero_raises_exception():
    calculator = SimpleCalculator()

    with pytest.raises(ValueError):
        calculator.mul(3, 0)        

def test_avg_of_iterable():
    numbers = range(10)
    calculator = SimpleCalculator()

    result = calculator.avg(numbers)
    assert result == 4.5

def test_avg_by_type_raises_exception():
    # varified by the "sum" function already, but it worths to keep the test here.
    calculator = SimpleCalculator()

    with pytest.raises(TypeError):
        calculator.avg(5)

def test_avg_by_upper_threshold():
    numbers = range(10)
    calculator = SimpleCalculator()

    result = calculator.avg(numbers, ut=8)
    assert result == 4.0

def test_avg_by_lower_threshold():
    numbers = range(10)
    calculator = SimpleCalculator()

    result = calculator.avg(numbers, lt=2)
    assert result == 5.5

def test_avg_upper_threshold_is_included():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], ut=98)
    assert result == 29.25

def test_avg_lower_threshold_is_included():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], lt=2)
    assert result == 29.25    

def test_avg_by_empty_iterable():
    numbers = []
    calculator = SimpleCalculator()

    result = calculator.avg(numbers)
    assert result == 0

def test_avg_by_empty_after_outlier_removal():
    numbers = [2, 5, 7, 11, 45, 65, 79]
    calculator = SimpleCalculator()

    result = calculator.avg(numbers, lt=15, ut=40)
    assert result == 0    

def test_avg_manages_empty_list_before_outlier_removal():
    calculator = SimpleCalculator()

    result = calculator.avg([], lt=15, ut=90)
    assert result == 0    

def test_avg_manages_zero_value_lower_outlier():
    calculator = SimpleCalculator()

    result = calculator.avg([-1, 0, 1], lt=0)
    assert result == 0.5    

def test_avg_accepts_generators():
    calculator = SimpleCalculator()

    result = calculator.avg(i for i in [2, 5, 12, 98])
    assert result == 29.25