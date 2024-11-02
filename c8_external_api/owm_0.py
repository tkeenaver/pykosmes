import requests
API_KEY = '5f511454578c093f1a83e27026deef70'  # OpenWeatherMap에서 발급받은 API 키
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()
if __name__ == '__main__':
    city = 'Seoul'
    weather_data = get_weather(city)
    print(weather_data)
