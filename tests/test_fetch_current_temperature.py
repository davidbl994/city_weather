import pytest
from weather_info import fetch_current_temperature

def test_fetch_current_temperature_valid_city():
    # Test that a valid city name returns a temperature
    print("Running test_fetch_current_temperature_valid_city")
    assert isinstance(fetch_current_temperature("Zagreb"), float)

def test_fetch_current_temperature_invalid_city():
    # Test that an invalid city name returns None
    print("Running test_fetch_current_temperature_invalid_city")
    assert fetch_current_temperature("asdasdsadas") is None

def test_fetch_current_temperature_empty_string():
    # Test that an empty string returns None
    print("Running test_fetch_current_temperature_empty_string")
    assert fetch_current_temperature("") is None

def test_fetch_current_temperature_spaces():
    # Test that a string of spaces returns None
    print("Running test_fetch_current_temperature_spaces")
    assert fetch_current_temperature("  ") is None

def test_fetch_current_temperature_special_characters():
    # Test that a string of spaces returns None
    print("Running test_fetch_current_temperature_special_characters")
    assert fetch_current_temperature("@#$%^&+()") is None
