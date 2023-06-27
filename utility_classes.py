# utility_classes.py

from settings import INITIAL_COIN_COUNT, REPRESENTATIVE_PORTION

class City:
    def __init__(self, country_count, country_index):
        self.__completed = False
        self.__country_count = country_count
        self.__neighbors = None

        self.__coins = [0] * country_count
        self.__cache = [0] * country_count

        self.__coins[country_index] = INITIAL_COIN_COUNT

    def update(self):
        for i in range(self.__country_count):
            self.__coins[i] += self.__cache[i]
            self.__cache[i] = 0

    def share_coins_with_neighbors(self):
        if all(coin_count > 0 for coin_count in self.__coins):
            self.__completed = True

        for i, coin_count in enumerate(self.__coins):
            if coin_count >= REPRESENTATIVE_PORTION:
                share = coin_count // REPRESENTATIVE_PORTION

                for neighbor_city in self.__neighbors:
                    neighbor_city.__cache[i] += share
                    self.__coins[i] -= share

    # Getters and Setters

    def set_neighbors(self, neighbors):
        self.__neighbors = neighbors

    def get_coins(self):
        return self.__coins

    def set_coins(self, coins):
        self.__coins = coins

    def get_cache(self):
        return self.__cache

    def set_cache(self, cache):
        self.__cache = cache

    def is_completed(self):
        return self.__completed
    

class Country:
    def __init__(self, name, lower_left_x, lower_left_y, upper_right_x, upper_right_y):
        self.name = name
        self.lower_left_x = lower_left_x
        self.lower_left_y = lower_left_y
        self.upper_right_x = upper_right_x
        self.upper_right_y = upper_right_y
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)

    def is_completed(self):
        return all(city.is_completed() for city in self.cities)
