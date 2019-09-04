from sqlalchemy import func

from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import CarReservation, User, Car, News
from rent_a_car.db_manager.result_set import queryset2list
from rent_a_car.user import get_user_by_id
import datetime


def get_users_list():
    """
    Get the list of all users
    :return: a list containing objects of type User
    """
    session = start_session()
    queryset = session.query(User)
    session.close()
    return queryset2list(queryset)


def get_all_reservations_list(reservation_filter):
    """
    Get the list of reservations
    :param reservation_filter: the filter to apply on reservations during the query
    :return: a list containing objects of type CarReservation
    """
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
    reservations_list = queryset2list(queryset)
    return sorted(reservations_list, key=lambda reservation: reservation.id_reservation, reverse=True)


def get_users_list_for_reservations_list(reservations_list):
    """
    Get the list of users that have a reservation in reservations_list
    :param reservations_list: the list of reservations
    :return: a list containing objects of type User
    """
    users_list = []
    for reservation in reservations_list:
        users_list.append(get_user_by_id(reservation.id_user))
    return users_list


def delete_car(car_id):
    """
    Delete the car specified by car_id
    :param car_id: the ID of car we want to delete
    :return: None
    """
    session = start_session()
    session.query(Car).filter(Car.id.__eq__(car_id)).delete()
    session.commit()
    session.close()
    delete_all_reservations_associated_to_car_id(car_id)


def update_car(car_id, brand, model, car_year, n_seats, car_type, engine, fuel, power, transmission, min_age, price,
               photo_name, preview):
    """
    Update the specs of the car specified by car_id
    :param car_id: the ID of the car we want to edit
    :param brand: the new car's brand
    :param model: the new car's model
    :param car_year: the new car's year
    :param n_seats: the new car's number of seats
    :param car_type: the new type of the car
    :param engine: the new engine displacement of the car
    :param fuel: the new car's type of fuel
    :param power: the new car's power
    :param transmission: the new car's transmission
    :param min_age: the new driver's minimum age for driving the car
    :param price: the new price of the car
    :param photo_name: the name of the new car's image
    :param preview: True if the admin want to show car in the home page
    :return: None
    """
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
    car.preview = preview
    if photo_name != "":
        car.photo_link = "/static/media/cars/" + photo_name
    session.commit()
    session.close()


def delete_all_reservations_associated_to_car_id(car_id):
    """
    Delete all the reservations associated with the car identified by car_id
    :param car_id: the ID of the car we have deleted
    :return: None
    """
    session = start_session()
    session.query(CarReservation).filter(CarReservation.id_car.__eq__(car_id)).delete()
    session.commit()
    session.close()


def delete_news(news_id):
    """
    Delete the news identified by news_id
    :param news_id: the ID of the new we want to delete
    :return: None
    """
    session = start_session()
    session.query(News).filter(News.id.__eq__(news_id)).delete()
    session.commit()
    session.close()


def save_news(news_content):
    """
    Save a new news into the database
    :param news_content: the text of the news
    :return: None
    """
    session = start_session()
    news = News(news_content)
    session.add(news)
    session.commit()
    session.close()


def update_account_type(user_id, account_type):
    """
    Update the privileges of the user identified by user_id
    :param user_id: the ID of the user we want to change his privileges
    :param account_type: admin or standard user
    :return: None
    """
    session = start_session()
    user = session.query(User).get(user_id)
    if account_type == 'admin':
        user.is_admin = True
    else:
        user.is_admin = False
    session.commit()
    session.close()


def add_car(brand, model, car_year, n_seats, car_type, engine, fuel, power, transmission, min_age, price, photo_name,
            preview):
    """
    Save a new car into the database
    :param brand: the car's brand
    :param model: the car's model
    :param car_year: the car's year
    :param n_seats: the number of seats of the car
    :param car_type: the type of the car
    :param engine: the engine displacement of the car
    :param fuel: the type of fuel of the car
    :param power: the power of the car
    :param transmission: the car's transmission
    :param min_age: the driver's minimum age for driving the car
    :param price: the price of the car
    :param photo_name: the link to the car's image
    :param preview:
    :return: True if the admin want to show car in the home page
    """
    photo_link = "/static/media/cars/" + photo_name
    session = start_session()
    new_car = Car(brand, model, car_year, n_seats, car_type, engine, fuel, power, transmission, min_age, price,
                  photo_link, preview)
    session.add(new_car)
    session.commit()
    queryset = session.query(func.max(Car.id).label("max_id"))
    res = queryset.one()
    session.close()
    return res.max_id
