from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import CarReservation, User, Car
from rent_a_car.db_manager.result_set import queryset2list
from rent_a_car.sign_up import get_age
from rent_a_car.home import get_car_identified_by_id
from datetime import datetime
from sqlalchemy import and_


def dates_intervals_are_overlapped(start_1, end_1, start_2, end_2):
    """
    Check if the date intervals are overlapped
    :param start_1: the date in which the first date interval starts
    :param end_1: the date in which the first date interval ends
    :param start_2: the date in which the second date interval starts
    :param end_2: the date in which the second date interval ends
    :return: True if date intervals are overlapped, False otherwise
    """
    return end_1 >= start_2 and end_2 >= start_1


def is_car_available_in_the_selected_period(date_from, date_to, car_id):
    """
    Check if the car identified by car_id is available in the selected period
    :param date_from: the date in which the rent will start
    :param date_to: the date in which the rent will end
    :param car_id: the car's ID
    :return: True if the car is available, False otherwise
    """
    session = start_session()
    queryset = session.query(CarReservation).filter(CarReservation.id_car.__eq__(car_id))
    reservations_list = queryset2list(queryset)
    try:
        date_from = datetime.strptime(date_from, '%Y-%m-%d')
        date_to = datetime.strptime(date_to, '%Y-%m-%d')
        is_available = True
        for reservation in reservations_list:
            if dates_intervals_are_overlapped(reservation.date_from, reservation.date_to, date_from.date(), date_to.date()):
                is_available = False
        return is_available
    except ValueError:
        return False


def calc_total_price(price_per_day, date_from, date_to):
    """
    Calculate the total price fot the rent
    :param price_per_day: the car's price per day
    :param date_from: the date in which the rent will start
    :param date_to: the date in which the rent will end
    :return: the total price for the rent
    """
    date_from = datetime.strptime(date_from, '%Y-%m-%d')
    date_to = datetime.strptime(date_to, '%Y-%m-%d')
    n_days = date_to - date_from
    n_days = n_days.days + 1
    return price_per_day * n_days


def get_total_price(reservation_id):
    """
    Get the rent's total price given the reservation id
    :param reservation_id: the reservation's id
    :return: the total price for the rent saved into the database
    """
    session = start_session()
    reservation = session.query(CarReservation).get(reservation_id)
    return reservation.price


def are_dates_valid(date_from, date_to):
    """
    Check if the inserted values are valid date values
    :param date_from: the date in which the rent will start
    :param date_to: the date in which the rent will end
    :return: True if dates are valid, False otherwise
    """
    if date_from > date_to or date_from == "" or date_to == "" or datetime.strptime(date_from, '%Y-%m-%d').date() < datetime.today().date():
        return False
    else:
        return True


def save_car_reservation(car_id, username, date_from, date_to):
    """
    Save the reservation into the database
    :param car_id: the ID of the car selected for the rent
    :param username: the username of the user that subscribed the reservation
    :param date_from: the date in which the rent will start
    :param date_to: the date in which the rent will end
    :return: None
    """
    car = get_car_identified_by_id(car_id)
    price = calc_total_price(car.price, date_from, date_to)
    session = start_session()
    new_car_reservation = CarReservation(car_id, username, date_from, date_to, price)
    session.add(new_car_reservation)
    session.commit()
    queryset = session.query(CarReservation).filter(and_(CarReservation.id_car.__eq__(car_id),
                                                         CarReservation.id_user.__eq__(username),
                                                         CarReservation.date_from.__eq__(date_from),
                                                         CarReservation.date_to.__eq__(date_to),
                                                         CarReservation.price.__eq__(price)))
    reservation = queryset2list(queryset)[0]
    session.close()
    return reservation.id_reservation


def has_user_age_requirement(username, car_id):
    """
    Check if the user identified by the username has the age to rent the car identified by car_id
    :param username: the user's email address
    :param car_id: the car's ID
    :return: True if the user has the age for renting the car, False otherwise
    """
    session = start_session()
    queryset = session.query(User).filter(User.id.__eq__(username))
    user = queryset2list(queryset)[0]
    queryset = session.query(Car).filter(Car.id.__eq__(car_id))
    car = queryset2list(queryset)[0]
    session.close()
    if get_age(str(user.birthdate)) >= car.min_age:
        return True
    else:
        return False


