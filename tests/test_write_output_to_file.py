import pytest
import os
from weather_info import write_output_to_file

def test_write_output_to_file():
    # Test that the function creates a file with the correct content
    city_name = "Paris"
    city_summary = "This is a test summary."
    current_temperature = 35.0
    write_output_to_file(city_name, city_summary, current_temperature)

    # Check that the file was created and has the correct content
    with open(f"{city_name}.txt", "r") as file:
        content = file.read()
    expected_content = f"{city_summary}\nCurrent temperature in {city_name} is {current_temperature} degrees Celsius."
    assert content == expected_content

    # Clean up the created file
    os.remove(f"{city_name}.txt")
