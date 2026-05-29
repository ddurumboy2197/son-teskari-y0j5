# test_reversal.py
import pytest
from reversal import reverse_numbers

@pytest.mark.parametrize("input, expected", [
    ([1, 2, 3], [3, 2, 1]),
    ([4, 5, 6], [6, 5, 4]),
    ([7, 8, 9], [9, 8, 7]),
    ([], []),
    ([1], [1]),
])
def test_reverse_numbers(input, expected):
    assert reverse_numbers(input) == expected

def test_reverse_numbers_negative():
    with pytest.raises(ValueError):
        reverse_numbers([-1, 2, 3])

def test_reverse_numbers_non_integer():
    with pytest.raises(TypeError):
        reverse_numbers([1.5, 2, 3])
