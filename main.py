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
    try:
        # Try to asks the user what latitude / longitude he has
        lat = float(input('Please enter your latitude: '))
        lon = float(input('Please enter your longitude: '))
        
        # If it worked, print a line for clarity and return the latitude / longitude 
        print('')
        return lat, lon
    
    except ValueError:
        # If a variable is entered incorrectly, print an error message and repeat the function
        print('Invalid input\nPlease enter a valid latitude and longitude.\n')
        return get_lat_lon()
  
try:
    # Try to read the 'API_KEY' environment variable from the .env file
    api_key = os.getenv('API_KEY')
    
    # Get the latitude / longitude
    lat, lon = get_lat_lon()

    # Get the weather data
    location, temperature, weather_description = get_weather_data(lat, lon, api_key)

    # Print the weather information
    print(f'In {location}, it is {temperature} ℃\nDescription: {weather_description}')

except ValueError as e:
    # If either value couldn't be read, catch the ValueError exception and print an error message
    print(f'There was an error while reading the environment variables.\n{e}')

except Exception as e:
    # If another unexpected error occurs, catch the general Exception exception and print an error message
    print(f'An unknown error occurred.\n{e}')