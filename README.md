# Weather Forecast with OpenWeatherMap API

This Python script makes a request to the OpenWeatherMap API and outputs the current temperature and weather conditions for a specified latitude and longitude.

## Installation

1. Download or clone the repository using `git clone`.
2. Ensure that you have Python 3.x installed.
3. Install the required Python modules using the command `pip install -r requirements.txt`.
4. Specify the desired latitude and longitude in the `.env` file.
5. Add your OpenWeatherMap API keys to the `.env` file.
6. Run the script using the command `python main.py`.

## Configuration

- You can obtain an API key from OpenWeatherMap by registering on the [OpenWeatherMap website](https://openweathermap.org/) and creating an account.
- Save your API key in the `.env` file as the `API_KEY` variable.

## Usage

- Run the script using the command `python main.py`.
- The script will output the current temperature and weather conditions for the specified latitude and longitude.
- If the request is successful, the script will output the data. Otherwise, an error message will be displayed.

## Credits

This script was created by Snasy and is licensed under the MIT License.
