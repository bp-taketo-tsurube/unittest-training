import pytest
from unittest.mock import patch
from datetime import datetime

from greeting.greeting import get_greeting


def test_greeting_morning():
    expected_message = "Good morning!"
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2025, 6, 4, 5, 0, 0)
        result = get_greeting()
        assert result == expected_message


def test_greeting_after():
    expected_message = "Good afternoon!"
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2025, 6, 4, 12, 0, 0)
        result = get_greeting()
        assert result == expected_message


def test_greeting_evening():
    expected_message = "Good evening!"
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2025, 6, 4, 18, 0, 0)
        result = get_greeting()
        assert result == expected_message


def test_greeting_night():
    expected_message = "Good night!"
    with patch("greeting.greeting.datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2025, 6, 4, 22, 0, 0)
        result = get_greeting()
        assert result == expected_message
