import os
from dotenv import load_dotenv
import requests

# Laden der Umgebungsvariablen aus der .env-Datei
load_dotenv()


try:
    #Versuche, die Umgebungsvariablen 'lat' und 'lon' aus der .env-Datei als float-Werte zu lesen
    lat = float(os.getenv('lat'))
    lon = float(os.getenv('lon'))
    
    #Versuche, die Umgebungsvariablen 'API_KEY' aus der .env-Datei zu lesen
    api_key = os.getenv('API_KEY')
    
except ValueError as e:
    #Wenn einer der Werte nicht gelesen werden konnte, fange die ValueError-Exception und gib eine Fehlermeldung aus.
    print('Es gab einen Fehler beim Lesen der Umgebungsvariablen.')
    print(e)
    
except Exception as e:
    #Wenn ein anderer, nicht erwarteter Fehler auftritt, fange die allgemeine Exception-Exception ab und gib eine Fehlermeldung aus.
    print('Ein unbekannter Fehler ist aufgetreten.')
    print(e)

    
try:
    # Versuche, die OpenWeatherMap API-Anfrage durchzuführen
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
    response.raise_for_status()
    
    # Extrahiere die notwendigen Daten aus der Antwort
    data = response.json()
    location = data['name']
    weather_description = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15)
    
    # Gib die Wetterinformationen aus
    print(f'In {location} sind es {temperature} ℃')
    print(f'Beschreibung: {weather_description}')

except requests.exceptions.HTTPError as e:
    # Wenn es einen HTTP-Fehler gibt, gebe den Statuscode der Antwort aus
    print(f'Fehler beim Abrufen der Wetterdaten. Statuscode: {response.status_code}')
    
except KeyError as e:
    # Wenn es einen Fehler bei der Verarbeitung der Daten gibt, gebe den KeyError aus
    print('Es gab einen Fehler beim Verarbeiten der Wetterdaten.')
    print(e)
    
except Exception as e:
    # Wenn es einen unbekannten Fehler gibt, gebe eine allgemeine Fehlermeldung aus
    print('Ein unbekannter Fehler ist aufgetreten.')
    print(e)
