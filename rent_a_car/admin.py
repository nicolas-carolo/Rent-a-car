from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import CarReservation, User, Car, News
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
    delete_all_reservations_associated_to_car_id(car_id)


def update_car(car_id, brand, model, car_year, n_seats, car_type, engine, fuel, power, transmission, min_age, price):
    session = start_session()
    car = session.query(Car).get(car_id)
    car.brand = brand
    car.model = model
    car.car_year = car_year
    car.n_seats = n_seats
    car.car_type = car_type
    car.engine = engine
    car.fuel = fuel
    car.power = power
    car.transmission = transmission
    car.min_age = min_age
    car.price = price
    session.commit()
    session.close()


def delete_all_reservations_associated_to_car_id(car_id):
    session = start_session()
    session.query(CarReservation).filter(CarReservation.id_car.__eq__(car_id)).delete()
    session.commit()
    session.close()


def delete_news(news_id):
    session = start_session()
    session.query(News).filter(News.id.__eq__(news_id)).delete()
    session.commit()
    session.close()


def save_news(news_content):
    session = start_session()
    news = News(news_content)
    session.add(news)
    session.commit()
    session.close()
