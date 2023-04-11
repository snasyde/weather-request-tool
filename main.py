# Wir importieren das os-Modul, das Funktionen bereitstellt, um auf Umgebungsvariablen und anderen Betriebssystemfunktionen zuzugreifen.
import os

# Wir importieren die load_dotenv-Funktion aus dem dotenv-Modul, um die Variablen aus der .env-Datei in die Umgebungsvariablen zu setzen.
from dotenv import load_dotenv

# Laden der Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Wir importieren das requests-Modul, um eine HTTP-Anfrage an die OpenWeatherMap-API zu stellen und Wetterdaten abzurufen.
import requests


respone = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={float(os.getenv('lat'))}&lon={float(os.getenv('lon'))}&appid={os.getenv('API_KEY')}')

data = respone.json()
location = data['name']
weather_description = data['weather'][0]['description']
temparature = round(data['main']['temp']-273.15)


if respone.status_code == 200:
    print('In '+location+' sind es '+str(temparature)+'℃')
    print('Beschreibung: '+weather_description)
else:
    print("Datenabfrage fehlgeschlagen.")
