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
    photo_link = Column(String)
    price = Column(Integer)
