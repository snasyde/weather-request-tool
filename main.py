import os
from dotenv import load_dotenv
import requests


# Load environment variables from the .env file
load_dotenv()

def get_weather_data(lat, lon, api_key):
    try:
        # Try to make the OpenWeatherMap API request
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
        response.raise_for_status()

        # Extract the necessary data from the response
        data = response.json()
        location = data['name']
        weather_description = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15)

        # Return the weather information
        return location, temperature, weather_description

    except requests.exceptions.HTTPError as e:
        # If there's an HTTP error, raise a custom exception with the response status code
        raise ValueError(f'Error while retrieving weather data. Status code: {response.status_code}')

    except (KeyError, IndexError) as e:
        # If there's an error processing the data, raise a custom exception
        raise ValueError('There was an error while processing the weather data.')

    except Exception as e:
        # If there's an unknown error, raise the original exception
        raise e

def get_lat_lon():
    # Asks the user what latitude / longitude he has
    lat = float(input('Your latitude: '))
    lon = float(input('Your longitude: '))
    
    # Return the latitude / longitude
    return lat, lon
        
try:
    # Try to read the 'API_KEY' environment variable from the .env file
    api_key = os.getenv('API_KEY')
    
    # Get the latitude / longitude
    lat, lon = get_lat_lon()

    # Get the weather data
    location, temperature, weather_description = get_weather_data(lat, lon, api_key)

    # Print the weather information
    print(f'In {location}, it is {temperature} ℃')
    print(f'Description: {weather_description}')

except ValueError as e:
    # If either value couldn't be read, catch the ValueError exception and print an error message
    print('There was an error while reading the environment variables.')
    print(e)

except Exception as e:
    # If another unexpected error occurs, catch the general Exception exception and print an error message
    print('An unknown error occurred.')
    print(e)
