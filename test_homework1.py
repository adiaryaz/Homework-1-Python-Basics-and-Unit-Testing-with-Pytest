import pytest

from homework1 import calculate_average, find_max, count_vowels, is_prime

def test_calculate_average():
    # Test normal list
    assert calculate_average([10, 20, 30, 40]) == 25.0
    # Test empty list
    assert calculate_average([]) == 0
    # Test list with one number
    assert calculate_average([15]) == 15.0
    # Test list with negative numbers
    assert calculate_average([5, -15, 10, -20]) == -5.0

def test_find_max():
    # Test normal list
    assert find_max([7, 14, 21, 3, 9]) == 21
    # Test empty list
    assert find_max([]) == None
    # Test List with all negative numbers
    assert find_max([-5, -12, -3, -1]) == -1
    # Test list with mixed negative and positive numbers
    assert find_max([-10, 5, -2, 8]) == 8

def test_count_vowels():
    assert count_vowels('hello') == 2
    assert count_vowels('HELLO') == 2
    assert count_vowels('bacod') == 2
    assert count_vowels("") == 0
    assert count_vowels('aiueoAIEOU') == 10

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-2) == False
    assert is_prime(-5) == False
