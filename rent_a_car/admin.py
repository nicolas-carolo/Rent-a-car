from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import CarReservation, User, Car
from rent_a_car.db_manager.result_set import queryset2list
from rent_a_car.user import get_user_by_id


def get_users_list():
    session = start_session()
    queryset = session.query(User)
    session.close()
    return queryset2list(queryset)


def get_all_reservations_list():
    session = start_session()
    queryset = session.query(CarReservation)
    session.close()
    return queryset2list(queryset)


def get_users_list_for_reservations_list(reservations_list):
    users_list = []
    for reservation in reservations_list:
        print(reservation.id_user)
        users_list.append(get_user_by_id(reservation.id_user))
    return users_list
