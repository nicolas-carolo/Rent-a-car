from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import CarReservation, User, Car
from rent_a_car.db_manager.result_set import queryset2list
from rent_a_car.sign_up import get_age
from datetime import datetime
from sqlalchemy import and_


def dates_intervals_are_overlapped(start_1, end_1, start_2, end_2):
    return end_1 >= start_2 and end_2 >= start_1


def is_car_available_in_the_selected_period(date_from, date_to, car_id):
    session = start_session()
    queryset = session.query(CarReservation).filter(CarReservation.id_car.__eq__(car_id))
    reservations_list = queryset2list(queryset)
    date_from = datetime.strptime(date_from, '%Y-%m-%d')
    date_to = datetime.strptime(date_to, '%Y-%m-%d')
    is_available = True
    for reservation in reservations_list:
        if dates_intervals_are_overlapped(reservation.date_from, reservation.date_to, date_from.date(), date_to.date()):
            is_available = False
    return is_available


def get_total_price(price_per_day, date_from, date_to):
    date_from = datetime.strptime(date_from, '%Y-%m-%d')
    date_to = datetime.strptime(date_to, '%Y-%m-%d')
    n_days = date_to - date_from
    n_days = n_days.days + 1
    return price_per_day * n_days


def are_dates_valid(date_from, date_to):
    if date_from > date_to or date_from == "" or date_to == "" or datetime.strptime(date_from, '%Y-%m-%d').date() < datetime.today().date():
        return False
    else:
        return True


def save_car_reservation(car_id, username, date_from, date_to):
    session = start_session()
    new_car_reservation = CarReservation(car_id, username, date_from, date_to)
    session.add(new_car_reservation)
    session.commit()
    queryset = session.query(CarReservation).filter(and_(CarReservation.id_car.__eq__(car_id),
                                                         CarReservation.id_user.__eq__(username),
                                                         CarReservation.date_from.__eq__(date_from),
                                                         CarReservation.date_to.__eq__(date_to)))
    reservation = queryset2list(queryset)[0]
    session.close()
    return reservation.id_reservation


def has_user_age_requirement(username, car_id):
    session = start_session()
    queryset = session.query(User).filter(User.id.__eq__(username))
    user = queryset2list(queryset)[0]
    queryset = session.query(Car).filter(Car.id.__eq__(car_id))
    car = queryset2list(queryset)[0]
    if get_age(str(user.birthdate)) >= car.min_age:
        return True
    else:
        return False

