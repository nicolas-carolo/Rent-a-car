from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import Car
from rent_a_car.db_manager.result_set import queryset2list
import datetime


def get_cars_list():
    session = start_session()
    queryset = session.query(Car)
    cars_list = queryset2list(queryset)
    session.close()
    return cars_list


def get_current_year():
    now = datetime.date.today()
    return now.year


def get_car_brands_list():
    session = start_session()
    queryset = session.query(Car)
    session.close()
    cars_list = queryset2list(queryset)
    brands_list = []
    for car in cars_list:
        brands_list.append(car.brand)
    brands_list = sorted(remove_duplicates_by_list(brands_list))
    for brand in brands_list:
        print(brand)
    return brands_list


def remove_duplicates_by_list(input_list):
    return list(dict.fromkeys(input_list))
