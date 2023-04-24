import requests
from user_location import get_user_location

def get_weather_data(api_key: str) -> dict:
    # Get the user's location information
    location = get_user_location()
    lat, lon = location['lat'], location['lon']

    # Define the API endpoint and parameters
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'lat': lat, 'lon': lon, 'appid': api_key, 'units': 'metric'}

    # Send a GET request to the API endpoint with the specified parameters
    response = requests.get(url, params=params)

    # If the API call was successful, parse the JSON response and extract the weather information
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']

        # Return the weather information as a dictionary
        return {'temperature': temperature, 'description': weather_description}

    # If the API call was unsuccessful, raise an exception with the error message
    else:
        raise Exception(f'API call failed with error code {response.status_code}: {response.text}')