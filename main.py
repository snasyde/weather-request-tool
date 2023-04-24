import os
from typing import Dict
from dotenv import load_dotenv

from extensions.weather_request import get_weather_data
from extensions.user_input import get_user_location

def get_api_key() -> str:
    # Load environment variables from the .env file
    load_dotenv()

    # Try to read the 'API_KEY' environment variable from the .env file
    api_key = os.getenv('API_KEY')

    if not api_key:
        # Raise a custom exception if the API_KEY environment variable is not set
        raise EnvironmentError("API_KEY environment variable is not set")

    return api_key

try:
    # Get the user's location
    location = get_user_location()

    # Get the weather data for the user's location
    weather_data: Dict[str, str] = get_weather_data(location['lat'], location['lon'], get_api_key())

    # Print the weather information
    print(f'In {location["name"]}, {location["country"]} it is {weather_data["temperature"]}℃\nDescription: {weather_data["description"]}')

except (EnvironmentError, ValueError) as e:
    # If an expected error occurs, print an error message
    print(f'Error: {e}')

except Exception as e:
    # If another unexpected error occurs, print an error message
    print(f'An unknown error occurred.\n{e}')