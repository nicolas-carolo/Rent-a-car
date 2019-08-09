from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import CarReservation, User, Car
from rent_a_car.db_manager.result_set import queryset2list


def get_user_by_id(user_id):
    session = start_session()
    queryset = session.query(User).filter(User.id.__eq__(user_id))
    session.close()
    return queryset2list(queryset)[0]