from typing import Dict

import geocoder

def get_user_location() -> Dict[str, float]:
    # Use the geocoder library to get the user's location
    g = geocoder.ip('me')

    # Extract the latitude, longitude, city, and country from the geocoder result
    lat, lon = g.latlng
    name, country = g.city, g.country

    # Return the location information as a dictionary
    return {'lat': lat, 'lon': lon, 'name': name, 'country': country}