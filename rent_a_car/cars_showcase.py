from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import Car
from rent_a_car.db_manager.result_set import queryset2list


def get_cars_list():
    session = start_session()
    queryset = session.query(Car)
    cars_list = queryset2list(queryset)
    session.close()
    return cars_list