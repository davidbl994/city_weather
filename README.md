# City Weather Information

This project provides information about a city including a short summary and the current temperature. The information is fetched from the OpenWeatherMap API and the Wikipedia API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3 installed on your machine. You also need the following Python packages:

- `pytest`
- `requests`
- `pip (Python package installer)`
- `pytest-html`

You can install them using pip:

```bash
pip install requests
```

```bash
pip install pytest
```

```bash
pip install pytest-html
```

or 

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Running the Script

To run the `weather_info.py` script, navigate to the project directory and run the following command:
```bash
python3 weather_info.py
```

When prompted, enter a city name. If the city name is valid, a new text file named after the city will
be created in the project directory (e.g. Berlin.txt). This file will contain the city summary and current temperature.

## Running the Tests

This project uses the pytest framework for testing. To run the tests, navigate to the project directory
and run the following command:

```bash
pytest -vs tests/
```

After the tests are executed, a HTML report will be generated in the results/ directory using the pytest-html library.

![test_report.png](test_report.png)




