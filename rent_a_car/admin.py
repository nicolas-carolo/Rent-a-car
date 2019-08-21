from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import CarReservation, User, Car
from rent_a_car.db_manager.result_set import queryset2list
from rent_a_car.user import get_user_by_id
import datetime


def get_users_list():
    session = start_session()
    queryset = session.query(User)
    session.close()
    return queryset2list(queryset)


def get_all_reservations_list(reservation_filter):
    today = datetime.datetime.today().date()
    session = start_session()
    if reservation_filter == "completed":
        queryset = session.query(CarReservation).filter(CarReservation.date_to < today)
    elif reservation_filter == "in-progress":
        queryset = session.query(CarReservation).filter(CarReservation.date_from <= today,
                                                        CarReservation.date_to >= today)
    elif reservation_filter == "reserved":
        queryset = session.query(CarReservation).filter(CarReservation.date_from > today)
    elif reservation_filter == "starting-today":
        queryset = session.query(CarReservation).filter(CarReservation.date_from == today)
    elif reservation_filter == "ending-today":
        queryset = session.query(CarReservation).filter(CarReservation.date_to == today)
    else:
        queryset = session.query(CarReservation)
    session.close()
    return queryset2list(queryset)


def get_users_list_for_reservations_list(reservations_list):
    users_list = []
    for reservation in reservations_list:
        users_list.append(get_user_by_id(reservation.id_user))
    return users_list


def delete_car(car_id):
    session = start_session()
    session.query(Car).filter(Car.id.__eq__(car_id)).delete()
    session.commit()
    session.close()
