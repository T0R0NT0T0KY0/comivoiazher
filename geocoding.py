import requests

from envs import API_KEY


def get_coordinates_by_city(city_name: str) -> (int, int):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={1}&appid={API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем наличие ошибок
        [data] = response.json()
        lat = data['lat']
        lon = data['lon']
        return lat, lon
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)

