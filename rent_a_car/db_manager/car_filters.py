from rent_a_car.db_manager.models import Car
from rent_a_car.sign_up import get_age
from sqlalchemy import and_


def filter_cars_by_brand(queryset, filter):
    queryset = queryset.filter(Car.brand.__eq__(filter))
    return queryset


def filter_cars_by_type(queryset, filter):
    queryset = queryset.filter(Car.car_type.__eq__(filter))
    return queryset


def filter_cars_by_n_seats(queryset, filter):
    queryset = queryset.filter(Car.n_seats.__eq__(filter))
    return queryset


def filter_cars_by_power(queryset, min_power, max_power):
    queryset = queryset.filter(and_(Car.power >= min_power, Car.power <= max_power))
    return queryset


def filter_cars_by_fuel(queryset, filter):
    queryset = queryset.filter(Car.fuel.__eq__(filter))
    return queryset


def filter_cars_by_transmission(queryset, filter):
    queryset = queryset.filter(Car.transmission.__eq__(filter))
    return queryset


def filter_cars_by_year(queryset, year_from, year_to):
    queryset = queryset.filter(and_(Car.car_year >= year_from, Car.car_year <= year_to))
    return queryset


def filter_cars_by_driver_min_age(queryset, driver_age):
    queryset = queryset.filter(Car.min_age <= driver_age)
    return queryset
