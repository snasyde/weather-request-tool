import os
from dotenv import load_dotenv
import requests

# Load environment variables from the .env file
load_dotenv()

try:
    # Try to read the 'lat' and 'lon' environment variables from the .env file as float values
    lat = float(os.getenv('lat'))
    lon = float(os.getenv('lon'))
    
    # Try to read the 'API_KEY' environment variable from the .env file
    api_key = os.getenv('API_KEY')
    
except ValueError as e:
    # If either value couldn't be read, catch the ValueError exception and print an error message
    print('There was an error while reading the environment variables.')
    print(e)
    
except Exception as e:
    # If another unexpected error occurs, catch the general Exception exception and print an error message
    print('An unknown error occurred.')
    print(e)

    
try:
    # Try to make the OpenWeatherMap API request
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
    response.raise_for_status()
    
    # Extract the necessary data from the response
    data = response.json()
    location = data['name']
    weather_description = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15)
    
    # Print the weather information
    print(f'In {location}, it is {temperature} ℃')
    print(f'Description: {weather_description}')

except requests.exceptions.HTTPError as e:
    # If there's an HTTP error, print the response status code
    print(f'Error while retrieving weather data. Status code: {response.status_code}')
    
except KeyError as e:
    # If there's an error processing the data, print the KeyError
    print('There was an error while processing the weather data.')
    print(e)
    
except Exception as e:
    # If there's an unknown error, print a general error message
    print('An unknown error occurred.')
    print(e)

