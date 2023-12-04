from csv_utils import write_to_csv, read_from_csv
import time

from comivoiazher import genetic_algorithm
from geocoding import get_coordinates_by_city

def write_coordinates():
    cities = ['London', 'Moskow', 'Kazan’', 'Washington', 'Nizhniy Novgorod', 'Paris']

    cities_coordinates = []

    for city in cities:
        lat, lon = get_coordinates_by_city(city)
        print(f'city: {city}. coordinates: {lat, lon}')
        cities_coordinates.append({'city': city, 'lat': lat, 'lon': lon})
        time.sleep(3)

    write_to_csv(cities_coordinates, 'cities_coordinates.csv')

def calculate_genetic_algorithm():
    cities_coordinates = read_from_csv('cities_coordinates.csv')

    best_route, min_distance = genetic_algorithm(cities_coordinates)

    print("Optimal Route:", list(map(lambda idx: cities_coordinates[idx]['city'], best_route)))
    print("Total Distance:", min_distance)


if __name__ == "__main__":
    write_coordinates()

    calculate_genetic_algorithm()
