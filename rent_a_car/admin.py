from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import CarReservation, User, Car
from rent_a_car.db_manager.result_set import queryset2list


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