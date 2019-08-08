from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import Car
from rent_a_car.db_manager.result_set import queryset2list
from rent_a_car.db_manager.car_filters import filter_cars_by_brand
from sqlalchemy import func
import datetime


def get_cars_list():
    session = start_session()
    queryset = session.query(Car)
    cars_list = queryset2list(queryset)
    session.close()
    return cars_list


def get_current_year():
    now = datetime.date.today()
    return now.year


def get_car_brands_list():
    cars_list = get_cars_list()
    brands_list = []
    for car in cars_list:
        brands_list.append(car.brand)
    brands_list = sorted(remove_duplicates_by_list(brands_list))
    return brands_list


def get_car_types_list():
    cars_list = get_cars_list()
    types_list = []
    for car in cars_list:
        types_list.append(car.car_type)
    types_list = sorted(remove_duplicates_by_list(types_list))
    return types_list


def get_car_n_seats_list():
    cars_list = get_cars_list()
    car_n_seats_list = []
    for car in cars_list:
        car_n_seats_list.append(car.n_seats)
    car_n_seats_list = sorted(remove_duplicates_by_list(car_n_seats_list))
    return car_n_seats_list


def get_fuel_list():
    cars_list = get_cars_list()
    fuel_list = []
    for car in cars_list:
        fuel_list.append(car.fuel)
    fuel_list = sorted(remove_duplicates_by_list(fuel_list))
    return fuel_list


def get_min_car_power_value():
    session = start_session()
    queryset = session.query(func.min(Car.power).label("min_value"))
    res = queryset.one()
    return res.min_value


def get_max_car_power_value():
    session = start_session()
    queryset = session.query(func.max(Car.power).label("max_value"))
    res = queryset.one()
    return res.max_value


def get_oldest_car_age():
    session = start_session()
    queryset = session.query(func.min(Car.car_year).label("oldest"))
    res = queryset.one()
    return res.oldest


def get_min_car_price_per_day():
    session = start_session()
    queryset = session.query(func.min(Car.price).label("min_value"))
    res = queryset.one()
    return res.min_value


def get_max_car_price_per_day():
    session = start_session()
    queryset = session.query(func.max(Car.price).label("max_value"))
    res = queryset.one()
    return res.max_value


def get_max_driver_age():
    session = start_session()
    queryset = session.query(func.max(Car.min_age).label("max_driver_age"))
    res = queryset.one()
    return res.max_driver_age


def remove_duplicates_by_list(input_list):
    return list(dict.fromkeys(input_list))


def filter_cars_by_user_parameters(brand):
    session = start_session()
    queryset = session.query(Car)
    queryset = filter_cars_by_brand(queryset, brand)
    return queryset2list(queryset)
