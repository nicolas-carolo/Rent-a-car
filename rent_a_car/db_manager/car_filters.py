from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import Car


def filter_cars_by_brand(queryset, brand):
    queryset = queryset.filter(Car.brand.__eq__(brand))
    return queryset
