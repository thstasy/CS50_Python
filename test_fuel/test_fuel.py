# from fuel import convert, gauge
# import pytest

# def test_input():
#     assert convert('1/2') == 50
#     assert convert('1/1') == 100
#     assert convert('0/10') == 0

# def test_errors():
#     with pytest.raises(ZeroDivisionError):
#          convert('2/0')
#     with pytest.raises(ValueError):
#          convert('3/2')

# def test_output():
#     assert gauge(1) == 'E'
#     assert gauge(100) == 'F'
#     assert gauge(50) == '50%'

from fuel import convert, gauge
import pytest

#convert expects a str in X/Y format as input
def test_convert():
    assert convert("0/4") == 0
    assert convert("1/100") == 1
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("99/100") == 99

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    with pytest.raises(ValueError):
        convert("cat/dog")



# gauge expects an int and returns a str that is:
# "E" if that int is less than or equal to 1,
# "F" if that int is greater than or equal to 99,
# and "Z%" otherwise
def test_gauge():
    assert gauge(0) == "E"
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"