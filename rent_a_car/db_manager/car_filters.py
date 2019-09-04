from rent_a_car.db_manager.models import Car
from rent_a_car.rent import is_car_available_in_the_selected_period
from sqlalchemy import and_


def filter_cars_by_brand(queryset, brand):
    """
    Filter the cars stored in the database by brand
    :param queryset: the queryset to filter
    :param brand: the name of the car brand desired
    :return: the filtered queryset
    """
    queryset = queryset.filter(Car.brand.__eq__(brand))
    return queryset


def filter_cars_by_type(queryset, car_type):
    """
    Filter the cars stored in the database by car type
    :param queryset: the queryset to filter
    :param car_type: the type of car desired
    :return: the filtered queryset
    """
    queryset = queryset.filter(Car.car_type.__eq__(car_type))
    return queryset


def filter_cars_by_n_seats(queryset, n_seats):
    """
    Filter the cars stored in the database by number of seats
    :param queryset: the queryset to filter
    :param n_seats: the number of seats desired
    :return: the filtered queryset
    """
    queryset = queryset.filter(Car.n_seats.__eq__(n_seats))
    return queryset


def filter_cars_by_power(queryset, min_power, max_power):
    """
    Filter the cars stored in the database by range of power
    :param queryset: the queryset to filter
    :param min_power: the minimum power desired
    :param max_power: the maximum power desired
    :return: the filtered queryset
    """
    queryset = queryset.filter(and_(Car.power >= min_power, Car.power <= max_power))
    return queryset


def filter_cars_by_fuel(queryset, fuel):
    """
    Filter the cars stored in the database by type of fuel
    :param queryset: the queryset to filter
    :param fuel: the type of fuel desired
    :return: the filtered queryset
    """
    queryset = queryset.filter(Car.fuel.__eq__(fuel))
    return queryset


def filter_cars_by_transmission(queryset, transmission):
    """
    Filter the cars stored in the database by transmission
    :param queryset: the queryset to filter
    :param transmission: the transmission desired
    :return: the filtered queryset
    """
    queryset = queryset.filter(Car.transmission.__eq__(transmission))
    return queryset


def filter_cars_by_year(queryset, year_from, year_to):
    """
    Filter the cars stored in the database by car range of years
    :param queryset: the queryset to filter
    :param year_from: the lower year bound
    :param year_to: the upper year bound
    :return: the filtered queryset
    """
    queryset = queryset.filter(and_(Car.car_year >= year_from, Car.car_year <= year_to))
    return queryset


def filter_cars_by_driver_min_age(queryset, driver_age):
    """
    Filter the cars stored in the database by driver's minimum age
    :param queryset: the queryset to filter
    :param driver_age: the driver's minimum age
    :return: the filtered queryset
    """
    queryset = queryset.filter(Car.min_age <= driver_age)
    return queryset


def filter_cars_by_price(queryset, min_price, max_price):
    """
    Filter the cars stored in the database by price
    :param queryset: the queryset to filter
    :param min_price: the car's minimum price
    :param max_price: the car's maximum price
    :return: the filtered queryset
    """
    queryset = queryset.filter(and_(Car.price >= min_price, Car.price <= max_price))
    return queryset


def filter_cars_by_rent_period(results_list, date_from, date_to):
    """
    Filter the cars stored in the database by date availability
    :param results_list: the queryset to filter
    :param date_from: the date in which the rent will start
    :param date_to: the date in which the rent will end
    :return:
    """
    results_list = list(results_list)
    for car in results_list:
        if not is_car_available_in_the_selected_period(date_from, date_to, car.id):
            results_list.remove(car)
    return results_list
