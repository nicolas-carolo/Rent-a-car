from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import Car
from rent_a_car.db_manager.result_set import queryset2list
from rent_a_car.db_manager.car_filters import filter_cars_by_brand, filter_cars_by_type, filter_cars_by_n_seats,\
    filter_cars_by_power, filter_cars_by_fuel, filter_cars_by_transmission, filter_cars_by_year,\
    filter_cars_by_driver_min_age, filter_cars_by_price, filter_cars_by_rent_period
from rent_a_car.rent import are_dates_valid
from sqlalchemy import func
import datetime


def get_cars_list():
    """
    Get the list of all cars saved into the database
    :return: a list containing objects of type Car
    """
    session = start_session()
    queryset = session.query(Car)
    cars_list = queryset2list(queryset)
    session.close()
    return cars_list


def get_current_year():
    """
    Get the current year
    :return: an object of type datetime.date
    """
    now = datetime.date.today()
    return now.year


def get_car_brands_list():
    """
    Get the list of all brands saved into database
    :return: a list containing all brands available
    """
    cars_list = get_cars_list()
    brands_list = []
    for car in cars_list:
        brands_list.append(car.brand)
    brands_list = sorted(remove_duplicates_by_list(brands_list))
    return brands_list


def get_car_types_list():
    """
    Get the list of all type of cars saved into the database
    :return: a list containing all types of cars available
    """
    cars_list = get_cars_list()
    types_list = []
    for car in cars_list:
        types_list.append(car.car_type)
    types_list = sorted(remove_duplicates_by_list(types_list))
    return types_list


def get_car_n_seats_list():
    """
    Get the list of all the number of seats saved into the database
    :return: a list containing all the number of seats available
    """
    cars_list = get_cars_list()
    car_n_seats_list = []
    for car in cars_list:
        car_n_seats_list.append(str(car.n_seats))
    car_n_seats_list = sorted(remove_duplicates_by_list(car_n_seats_list))
    return car_n_seats_list


def get_fuel_list():
    """
    Get the list of type of fuels saved into the database
    :return: a list containing all the type of fuels available
    """
    cars_list = get_cars_list()
    fuel_list = []
    for car in cars_list:
        fuel_list.append(car.fuel)
    fuel_list = sorted(remove_duplicates_by_list(fuel_list))
    return fuel_list


def get_min_car_power_value():
    """
    Get the car's minimum power available
    :return: the car's minimum power
    """
    session = start_session()
    queryset = session.query(func.min(Car.power).label("min_value"))
    res = queryset.one()
    return res.min_value


def get_max_car_power_value():
    """
    Get the car's maximum power available
    :return: the car's maximum power
    """
    session = start_session()
    queryset = session.query(func.max(Car.power).label("max_value"))
    res = queryset.one()
    return res.max_value


def get_oldest_car_age():
    """
    Get the car's year of the oldest car
    :return: the car's year of the oldest car
    """
    session = start_session()
    queryset = session.query(func.min(Car.car_year).label("oldest"))
    res = queryset.one()
    return res.oldest


def get_min_car_price_per_day():
    """
    Get the car's minimum price per day available
    :return: the car's minimum price per day available
    """
    session = start_session()
    queryset = session.query(func.min(Car.price).label("min_value"))
    res = queryset.one()
    return res.min_value


def get_max_car_price_per_day():
    """
    Get the car's maximum price per day available
    :return: the car's maximum price per day available
    """
    session = start_session()
    queryset = session.query(func.max(Car.price).label("max_value"))
    res = queryset.one()
    return res.max_value


def remove_duplicates_by_list(input_list):
    """
    Remove the duplicates from the input list
    :param input_list: the input list
    :return: the input list without duplicates
    """
    return list(dict.fromkeys(input_list))


def filter_cars_by_user_parameters(brand, car_type, n_seats, min_power, max_power, fuel, transmission, car_year_from,
                                   car_year_to, driver_age, min_price, max_price, date_from, date_to):
    """
    Filters the cars available by the parameters inserted by the user
    :param brand: the brand inserted by the user
    :param car_type: the type of the car inserted by the user
    :param n_seats: the number of seats inserted by the user
    :param min_power: the car's minimum power inserted by the user
    :param max_power: the car's maximum power inserted by the user
    :param fuel: the type of fuel inserted by the user
    :param transmission: the car's transmission inserted by the user
    :param car_year_from: the lower car's year bound inserted by the user
    :param car_year_to: the upper car's year bound inserted by the user
    :param driver_age: the driver's minimum age inserted by the user
    :param min_price: the car's minimum price per day inserted by the user
    :param max_price: the car's maximum price per day inserted by the user
    :param date_from: the date in which the rent will start
    :param date_to: the date in which the rent will end
    :return: the list containing the cars that respect the parameters inserted by the user
    """
    session = start_session()
    queryset = session.query(Car)
    if brand != 'all':
        queryset = filter_cars_by_brand(queryset, brand)
    if car_type != 'all':
        queryset = filter_cars_by_type(queryset, car_type)
    if n_seats != 'all':
        queryset = filter_cars_by_n_seats(queryset, n_seats)
    queryset = filter_cars_by_power(queryset, min_power, max_power)
    if fuel != 'all':
        queryset = filter_cars_by_fuel(queryset, fuel)
    if transmission != 'all':
        queryset = filter_cars_by_transmission(queryset, transmission)
    queryset = filter_cars_by_year(queryset, car_year_from, car_year_to)
    if driver_age != "none":
        queryset = filter_cars_by_driver_min_age(queryset, driver_age)
    queryset = filter_cars_by_price(queryset, min_price, max_price)
    results_list = queryset2list(queryset)
    if are_dates_valid(date_from, date_to):
        results_list = filter_cars_by_rent_period(results_list, date_from, date_to)
    return results_list
