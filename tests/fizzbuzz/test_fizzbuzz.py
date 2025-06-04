from fizzbuzz.fizzbuzz import fizzbuzz
import pytest


# 3の倍数「Fizz」
def test_fizzbuzz_example():
    # Arrange
    input_value = 3
    expected_output = "Fizz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# 5の倍数「Buzz」
def test_fizzbuzz_five():
    # Arrange
    input_value = 5
    expected_output = "Buzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# n15
def test_fizzbuzz_15():
    # Arrange
    input_value = 15
    expected_output = "FizzBuzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# nnot 3 5
def test_fizzbuzz_7():
    # Arrange
    input_value = 7
    expected_output = "7"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


def test_fizzbuzz_0():
    # Arrange
    input_value = 0
    # expected_output = ValueError

    # Act
    with pytest.raises(ValueError) as e:
        result = fizzbuzz(input_value)

    # Assert
    assert str(e.value) == "n must be between 1 and 1000."


def test_fizzbuzz_1001():
    # Arrange
    input_value = 1001
    # expected_output = ValueError

    # Act
    with pytest.raises(ValueError) as e:
        result = fizzbuzz(input_value)

    # Assert
    assert str(e.value) == "n must be between 1 and 1000."


def test_fizzbuzz_str():
    # Arrange
    input_value = "a"
    # expected_output = ValueError

    # Act
    with pytest.raises(TypeError) as e:
        result = fizzbuzz(input_value)

    # Assert
    assert str(e.value) == "n must be an integer."


# n<1
# n>1000
# n not integer
