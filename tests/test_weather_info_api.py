import os
import pytest
import requests
import sys

# Add the main directory to the sys path to import config.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config  # Import the configuration module

def test_weather_api():
    # Define the city name and get the API key from config module
    city_name = 'Tokio'
    api_key = config.WEATHER_API_KEY

    # Make a request to the weather API
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")

    # Print the status code of the response
    print(f"Weather API response status code: {response.status_code}")
    assert response.status_code == 200

    # Parse the response data as JSON
    data = response.json()

    # Assert that the 'main' and 'temp' keys are present in the data
    assert 'main' in data
    assert 'temp' in data['main']

def test_wikipedia_api():
    # Define the city name
    city_name = 'Tokio'

    # Make a request to the Wikipedia API
    response = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{city_name}")

    # Print the status code of the response
    print(f"Wikipedia API response status code: {response.status_code}")
    assert response.status_code == 200

    # Parse the response data as JSON
    data = response.json()

    # Assert that the 'extract' key is present in the data
    assert 'extract' in data

    # Print the response data
    print(f"Wikipedia API response data: {data}")
