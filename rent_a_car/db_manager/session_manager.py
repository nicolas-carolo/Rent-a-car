import sqlalchemy
from sqlalchemy.orm import sessionmaker


def start_session():
    """
    Start a new database session.
    :return: a new database session.
    """
    engine = sqlalchemy.create_engine('mysql+pymysql://rentacar-user:rent-a-car1@localhost:3306/RENTACAR')
    Session = sessionmaker(bind=engine)
    return Session()
