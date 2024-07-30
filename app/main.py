class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    # def serve_cars(self, cars_list: list):


    def calculate_washing_price(self, car: Car):
        cost = (car.comfort_class
                * (self.clean_power
                - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center)
        return round(cost, 1)

    # def wash_single_car(self):


    # def rate_service(self):