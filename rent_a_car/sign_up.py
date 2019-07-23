from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import User, UserSession
from rent_a_car.db_manager.result_set import queryset2list
from datetime import date, datetime


def create_account(name, surname, birthdate, username, password, retype_password):
    error_msg = "Subscription failed!"
    error_msg = validate_sign_up_data(name, surname, birthdate, username, password, retype_password, error_msg)
    if error_msg == "OK":
        session = start_session()
        new_user = User(username, password, surname, name, birthdate)
        session.add(new_user)
        session.commit()
        session.close()
        return "OK"
    else:
        return error_msg


def validate_sign_up_data(name, surname, birthdate, username, password, retype_password, error_msg):
    if is_blank_input(name) or is_blank_input(surname) or is_blank_input(birthdate) or is_blank_input(username) or is_blank_input(password) or is_blank_input(retype_password):
        return error_msg + " The form has not been completely filled."
    if get_age(birthdate) < 18:
        return error_msg + " You have not 18."
    if password != retype_password:
        return error_msg + " Passwords do not match."
    session = start_session()
    queryset = session.query(User).filter(User.id.__eq__(username))
    session.close()
    users_list = queryset2list(queryset)
    if users_list.__len__() == 0:
        return "OK"
    else:
        return error_msg + " There is already another user subscribed with this email address."


def is_blank_input(input):
    if input == "" or str(input).isspace():
        return True
    else:
        return False


def get_age(birthdate):
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
