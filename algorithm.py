# algorithm.py

from utility_classes import City, Country
from settings import MAX_XY_VALUE, MAX_NAME_LENGTH
class Algorithm:
    def __init__(self):
        self.country_list = []

    def create_empty_area(self):
        xs = []
        ys = []

        for country in self.country_list:
            xs.extend((country.lower_left_x, country.upper_right_x))
            ys.extend((country.lower_left_y, country.upper_right_y))

        y_range = range(max(ys) - min(ys) + 1)
        x_range = range(max(xs) - min(xs) + 1)

        return [[None for _ in y_range] for _ in x_range]

    def create_cities(self, area):
        country_count = len(self.country_list)
        country_index = 0

        for country in self.country_list:
            for i in range(country.upper_right_x - country.lower_left_x + 1):
                for j in range(country.upper_right_y - country.lower_left_y + 1):
                    x = country.lower_left_x + i
                    y = country.lower_left_y + j

                    city = City(country_count, country_index, country.name)

                    area[x][y] = city
                    country.add_city(city)

            country_index += 1

    def get_neighbors(self, area, x, y):
        width = len(area)
        height = len(area[0])
        neighbors = []

        if x + 1 <= width - 1 and area[x + 1][y]:
            neighbors.append(area[x + 1][y])

        if x - 1 >= 0 and area[x - 1][y]:
            neighbors.append(area[x - 1][y])

        if y + 1 <= height - 1 and area[x][y + 1]:
            neighbors.append(area[x][y + 1])

        if y - 1 >= 0 and area[x][y - 1]:
            neighbors.append(area[x][y - 1])

        return neighbors

    def add_neighbors(self, area):
        width = len(area)
        height = len(area[0])

        for x in range(width):
            for y in range(height):
                city = area[x][y]

                if city:
                    neighbors = self.get_neighbors(area, x, y)
                    city.set_neighbors(neighbors)

    def init_algorithm(self):
        area = self.create_empty_area()
        self.create_cities(area)
        self.add_neighbors(area)

    def is_completed(self):
        return all(map(lambda country: country.is_completed(), self.country_list))
    
    @staticmethod
    def check_max_value(country_name, value, coord):
        if not 1 <= value <= MAX_XY_VALUE:
            raise Exception(f'In {country_name}: value {value} is not in range 1 ≤ {coord} ≤ {MAX_XY_VALUE}')

    @staticmethod
    def check_range(country_name, value_l, value_h, coord_l, coord_h):
        if value_l > value_h:
            raise Exception(f'In {country_name}: value {coord_l}:{value_l} > {coord_h}:{value_h}')

    def add_country(self, string):
        name, *coordinates = string.split()

        if len(name) > MAX_NAME_LENGTH:
            raise Exception('Name has more than 25 characters')

        xl, yl, xh, yh = map(int, coordinates)

        Algorithm.check_max_value(name, xl, 'xl')
        Algorithm.check_max_value(name, yl, 'yl')
        Algorithm.check_max_value(name, xh, 'xh')
        Algorithm.check_max_value(name, yh, 'yh')

        Algorithm.check_range(name, xl, xh, 'xl', 'xh')
        Algorithm.check_range(name, yl, yh, 'yl', 'yh')

        self.country_list.append(Country(name, xl - 1, yl - 1, xh - 1, yh - 1))

    def check_islands(self):
        if len(self.country_list) != 1:
            for country in self.country_list:
                if country.is_island():
                    raise Exception(f'Country {country.name} is an island')

    def run(self):
        self.init_algorithm()
        self.check_islands()
        result = {}
        days = 0

        while True:
            for country in self.country_list:
                for city in country.cities:
                    city.share_coins_with_neighbors()

                if country.is_completed():
                    if country.name not in result:
                        result[country.name] = days

            if self.is_completed():
                break

            for country in self.country_list:
                for city in country.cities:
                    city.update()

            days += 1

        return sorted(result.items(), key=lambda x: (x[1], x[0]))
    
