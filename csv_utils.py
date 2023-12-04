import csv


def read_from_csv(filename='cities_coordinates.csv'):
    cities_data = []

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cities_data.append({
                'city': row['city'],
                'lat': float(row['lat']),
                'lon': float(row['lon']),
            })

    return cities_data

def write_to_csv(data, filename='cities_coordinates.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['city', 'lat', 'lon']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for city_data in data:
            writer.writerow(city_data)