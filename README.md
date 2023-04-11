# Wettervorhersage mit OpenWeatherMap API

Dieses Python-Skript stellt eine Anfrage an die OpenWeatherMap-API und gibt die aktuelle Temperatur und Wetterbedingungen für einen bestimmten Breiten- und Längengrad aus.

## Installation

1. Laden Sie das Repository herunter oder klonen Sie es mit `git clone`.
2. Stellen Sie sicher, dass Sie Python 3.x installiert haben.
3. Installieren Sie die benötigten Python-Module mit dem Befehl `pip install -r requirements.txt`.
4. Geben Sie die gewünschte Breite und Länge in der `.env`-Datei an.
5. Fügen Sie Ihre OpenWeatherMap-API-Schlüssel in der `.env`-Datei hinzu.
6. Führen Sie das Skript mit dem Befehl `python main.py` aus.

## Konfiguration

- Die Breite und Länge müssen als Dezimalzahlen in der `.env`-Datei angegeben werden.
- Sie können einen API-Schlüssel von OpenWeatherMap erhalten, indem Sie sich auf der [OpenWeatherMap-Website](https://openweathermap.org/) registrieren und ein Konto erstellen.
- Speichern Sie Ihren API-Schlüssel in der `.env`-Datei als `API_KEY`-Variable.

## Verwendung

- Führen Sie das Skript mit dem Befehl `python main.py` aus.
- Das Skript gibt die aktuelle Temperatur und Wetterbedingungen für die angegebenen Breiten- und Längengrade aus.
- Wenn die Abfrage erfolgreich ist, gibt das Skript die Daten aus. Andernfalls wird eine Fehlermeldung angezeigt.

## Credits

Dieses Skript wurde von Snasy erstellt und ist unter der MIT-Lizenz lizenziert.
