from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import User, UserSession
from rent_a_car.db_manager.result_set import queryset2list
from datetime import date, datetime


def create_account(name, surname, birthdate, username, password, retype_password):
    if validate_sign_up_data(name, surname, birthdate, username, password, retype_password):
        session = start_session()
        new_user = User(username, password, surname, name, birthdate)
        session.add(new_user)
        session.commit()
        session.close()
        return True
    else:
        return False


def validate_sign_up_data(name, surname, birthdate, username, password, retype_password):
    if is_blank_input(name) or is_blank_input(surname) or is_blank_input(birthdate) or is_blank_input(username) or is_blank_input(password) or is_blank_input(retype_password):
        return False
    if get_age(birthdate) < 18:
        return False
    if password != retype_password:
        return False
    session = start_session()
    queryset = session.query(User).filter(User.id.__eq__(username))
    session.close()
    users_list = queryset2list(queryset)
    if users_list.__len__() == 0:
        return True
    else:
        return False


def is_blank_input(input):
    if input == "" or str(input).isspace():
        return True
    else:
        return False


def get_age(birthdate):
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
