import math
import random

def calculate_distance(city1, city2):
    # Рассчитываем расстояние между двумя городами по формуле гаверсинуса
    R = 6371  # Средний радиус Земли в километрах
    lat1, lon1 = math.radians(city1['lat']), math.radians(city1['lon'])
    lat2, lon2 = math.radians(city2['lat']), math.radians(city2['lon'])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

def total_distance(route, cities):
    distance = 0
    for i in range(len(route) - 1):
        distance += calculate_distance(cities[route[i]], cities[route[i + 1]])
    distance += calculate_distance(cities[route[-1]], cities[route[0]])  # Замыкаем маршрут
    return distance

# генерирует случайный маршрут перестановкой номеров городов
def generate_individual(num_cities):
    individual = list(range(num_cities))
    random.shuffle(individual)
    return individual

# скрещивания между двумя родителями, создавая потомка.
# В данном случае используется одноточечное скрещивание
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
    return child

# мутацию на индивиде, меняя местами два случайных города.
def mutate(individual):
    mutation_point1 = random.randint(0, len(individual) - 1)
    mutation_point2 = random.randint(0, len(individual) - 1)
    individual[mutation_point1], individual[mutation_point2] = individual[mutation_point2], individual[mutation_point1]
    return individual

def genetic_algorithm(cities, population_size=50, generations=1000):
    num_cities = len(cities)
    population = [generate_individual(num_cities) for _ in range(population_size)]

    for generation in range(generations):
        population = sorted(population, key=lambda x: total_distance(x, cities))

        # Выбираем лучшие особи для размножения
        elite_size = int(0.1 * population_size)
        elite = population[:elite_size]

        # Создаем новое поколение
        offspring = elite.copy()

        while len(offspring) < population_size:
            parent1 = random.choice(elite)
            parent2 = random.choice(elite)
            child = crossover(parent1, parent2)
            if random.random() < 0.2:  # Вероятность мутации
                child = mutate(child)
            offspring.append(child)

        population = offspring

    best_route = min(population, key=lambda x: total_distance(x, cities))
    min_distance = total_distance(best_route, cities)

    return best_route, min_distance