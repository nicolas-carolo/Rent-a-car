from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Car(Base):
    """
    The database object Car
    """
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(Integer)
    car_year = Column(Integer)
    n_seats = Column(Integer)
    car_type = Column(String)
    min_age = Column(Integer)
    engine = Column(String)
    fuel = Column(String)
    power = Column(String)
    transmission = Column(String)
    photo_link = Column(String)
    price = Column(Integer)
    preview = Column(Integer)

    def __init__(self, brand, model, car_year, n_seats, car_type, engine, fuel, power, transmission, min_age, price,
                 photo_link, preview):
        self.brand = brand
        self.model = model
        self.car_year = car_year
        self.n_seats = n_seats
        self.car_type = car_type
        self.engine = engine
        self.fuel = fuel
        self.power = power
        self.transmission = transmission
        self.min_age = min_age
        self.price = price
        self.photo_link = photo_link
        self.preview = preview


class News(Base):
    """
    The database object news
    """
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    description = Column(String)

    def __init__(self, description):
        self.description = description


class CarReservation(Base):
    """
    The database object car reservation
    """
    __tablename__ = 'car_reservations'

    id_reservation = Column(Integer, primary_key=True)
    id_car = Column(Integer)
    id_user = Column(String)
    date_from = Column(String)
    date_to = Column(String)
    price = Column(Integer)

    def __init__(self, id_car, id_user, date_from, date_to, price):
        self.id_car = id_car
        self.id_user = id_user
        self.date_from = date_from
        self.date_to = date_to
        self.price = price


class UserSession(Base):
    """
    The database object session
    """
    __tablename__ = 'sessions'

    id_session = Column(String, primary_key=True)
    id_user = Column(String)

    def __init__(self, id_session, id_user):
        self.id_session = id_session
        self.id_user = id_user


class User(Base):
    """
    The database object user
    """
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    password = Column(String)
    surname = Column(String)
    name = Column(String)
    birthdate = Column(String)
    is_admin = Column(Integer)

    def __init__(self, id, password, surname, name, birthdate, is_admin):
        self.id = id
        self.password = password
        self.surname = surname
        self.name = name
        self.birthdate = birthdate
        self.is_admin = is_admin
