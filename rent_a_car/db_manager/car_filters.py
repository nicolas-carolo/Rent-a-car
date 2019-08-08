from rent_a_car.db_manager.models import Car
from rent_a_car.rent import is_car_available_in_the_selected_period
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


def filter_cars_by_price(queryset, min_price, max_price):
    queryset = queryset.filter(and_(Car.price >= min_price, Car.price <= max_price))
    return queryset


def filter_cars_by_rent_period(results_list, date_from, date_to):
    results_list = list(results_list)
    for car in results_list:
        if not is_car_available_in_the_selected_period(date_from, date_to, car.id):
            results_list.remove(car)
    return results_list
