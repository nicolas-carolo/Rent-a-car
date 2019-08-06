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
    plate = Column(String)
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


class News(Base):
    """
    The database object news
    """
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    description = Column(String)


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

    def __init__(self, id_car, id_user, date_from, date_to):
        self.id_car = id_car
        self.id_user = id_user
        self.date_from = date_from
        self.date_to = date_to


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

    def __init__(self, id, password, surname, name, birthdate):
        self.id = id
        self.password = password
        self.surname = surname
        self.name = name
        self.birthdate = birthdate
