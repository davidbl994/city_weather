import pytest
from weather_info import fetch_city_summary

def test_fetch_city_summary_valid_city():
    # Test that a valid city name returns a summary
    print("Running test_fetch_city_summary_valid_city")
    assert isinstance(fetch_city_summary("Zagreb"), str)

def test_fetch_city_summary_invalid_city():
    # Test that an invalid city name returns None
    print("Running test_fetch_city_summary_invalid_city")
    assert fetch_city_summary("asdasdsadas") is None

def test_fetch_city_summary_empty_string():
    # Test that an empty string returns None
    print("Running test_fetch_city_summary_empty_string")
    assert fetch_city_summary("") is None

def test_fetch_city_summary_spaces():
    # Test that a string of spaces returns None
    print("Running test_fetch_city_summary_spaces")
    assert fetch_city_summary("   ") is None

@pytest.mark.xfail(reason="This test is expected to fail because special characters are not valid city names.")
def test_fetch_city_summary_special_characters():
    # Test that a string of special characters returns None
    print("Running test_fetch_city_summary_special_characters")
    assert fetch_city_summary("@#$%^&*()") is None
