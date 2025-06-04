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


# n not 3 5
def test_fizzbuzz_7():
    # Arrange
    input_value = 7
    expected_output = "7"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


# n<1
def test_fizzbuzz_0():
    # Arrange
    input_value = 0
    expected_output = "n must be between 1 and 1000."

    # Act
    with pytest.raises(ValueError) as e:
        fizzbuzz(input_value)

    # Assert
    assert str(e.value) == expected_output


# n>1000
def test_fizzbuzz_1001():
    # Arrange
    input_value = 1001
    expected_output = "n must be between 1 and 1000."

    # Act
    with pytest.raises(ValueError) as e:
        fizzbuzz(input_value)

    # Assert
    assert str(e.value) == expected_output


# n not integer (str)
def test_fizzbuzz_str():
    # Arrange
    input_value = "a"
    expected_output = "n must be an integer."

    # Act
    with pytest.raises(TypeError) as e:
        fizzbuzz(input_value)

    # Assert
    assert str(e.value) == expected_output
