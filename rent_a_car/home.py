from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import Car, News
from rent_a_car.db_manager.result_set import queryset2list


def get_cars_preview():
    session = start_session()
    queryset = session.query(Car).filter(Car.preview.__eq__(True))
    cars_list = queryset2list(queryset)
    session.close()
    return cars_list


def get_news_list():
    session = start_session()
    queryset = session.query(News)
    news_list = queryset2list(queryset)
    session.close()
    return news_list


def get_car_identified_by_id(id):
    session = start_session()
    queryset = session.query(Car).filter(Car.id.__eq__(id))
    car = queryset2list(queryset)[0]
    session.close()
    return car


