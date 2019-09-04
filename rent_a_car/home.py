from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import Car, News
from rent_a_car.db_manager.result_set import queryset2list


def get_cars_preview():
    """
    Get the cars to show in the home poge
    :return: the list of cars to show in the home page
    """
    session = start_session()
    queryset = session.query(Car).filter(Car.preview.__eq__(True))
    cars_list = queryset2list(queryset)
    session.close()
    return cars_list


def get_news_list():
    """
    Get the news
    :return: a list containing all the news
    """
    session = start_session()
    queryset = session.query(News)
    news_list = queryset2list(queryset)
    session.close()
    return sorted(news_list, key=lambda news: news.id, reverse=True)
    return news_list


def get_car_identified_by_id(id):
    """
    Get the car identified by the id
    :param id: the ID of the car we want to get
    :return: the desired object of type Car
    """
    session = start_session()
    queryset = session.query(Car).filter(Car.id.__eq__(id))
    car = queryset2list(queryset)[0]
    session.close()
    return car


