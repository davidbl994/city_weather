import config
import requests

# Function to get the city name from the user
def get_city_name():
    return input("Enter the city name: ")

# Function to fetch the current temperature of a given city from the OpenWeatherMap API
def fetch_current_temperature(city_name):
    api_key = config.WEATHER_API_KEY  # Use the API key from the config module
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
    if response.status_code != 200:
        return None
    data = response.json()
    temp_in_celsius = data['main']['temp'] - 273.15  # Convert temperature from Kelvin to Celsius
    return round(temp_in_celsius, 1)

# Function to fetch the summary of a given city from the Wikipedia API
def fetch_city_summary(city_name):
    response = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{city_name}")
    if response.status_code != 200:
        return None
    data = response.json()
    return data['extract']

# Function to write the city summary and current temperature to a file
def write_output_to_file(city_name, city_summary, current_temperature):
    with open(f"{city_name}.txt", "w") as file:
        file.write(f"{city_summary}\n")
        file.write(f"Current temperature in {city_name} is {current_temperature} degrees Celsius.")

# Main function to get the city name, fetch the temperature and summary, and write them to a file
def main():
    city_name = get_city_name()
    current_temperature = fetch_current_temperature(city_name)
    city_summary = fetch_city_summary(city_name)
    if current_temperature is None or city_summary is None:
        print("Invalid city name. Please enter a valid city name.")
    else:
        write_output_to_file(city_name, city_summary, current_temperature)


if __name__ == "__main__":
    main()
