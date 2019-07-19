from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import Reservation
from rent_a_car.db_manager.result_set import queryset2list
from datetime import datetime


def dates_intervals_are_overlapped(start_1, end_1, start_2, end_2):
    print(start_1, end_1, start_2, end_2, end_1 >= start_2 and end_2 >= start_1)
    return end_1 >= start_2 and end_2 >= start_1


def is_car_available_in_the_selected_period(date_from, date_to, car_id):
    session = start_session()
    queryset = session.query(Reservation).filter(Reservation.id_car.__eq__(car_id))
    reservations_list = queryset2list(queryset)
    print(date_from, date_to)
    date_from = datetime.strptime(date_from, '%Y-%m-%d')
    date_to = datetime.strptime(date_to, '%Y-%m-%d')
    print(type(date_from), type(date_to), type(reservations_list[0].date_from), type(reservations_list[0].date_to))
    is_available = True
    for reservation in reservations_list:
        if dates_intervals_are_overlapped(reservation.date_from, reservation.date_to, date_from.date(), date_to.date()):
            is_available = False

    return is_available
