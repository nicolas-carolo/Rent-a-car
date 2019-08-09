from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import CarReservation, User, Car
from rent_a_car.db_manager.result_set import queryset2list
from rent_a_car.sign_up import is_blank_input, get_age


def get_user_by_id(user_id):
    session = start_session()
    queryset = session.query(User).filter(User.id.__eq__(user_id))
    session.close()
    return queryset2list(queryset)[0]


def edit_user_info(name, surname, birthdate, old_username, new_username):
    if is_blank_input(name) or is_blank_input(surname) or is_blank_input(birthdate) or is_blank_input(new_username):
        return "Error: The form has not been completely filled."
    if get_age(birthdate) < 18:
        return "Error: The age value must be greater than or equal to 18."
    session = start_session()
    user = session.query(User).get(old_username)
    if old_username != new_username:
        queryset = session.query(User).filter(User.id.__eq__(new_username))
        users_list = queryset2list(queryset)
        if users_list.__len__() == 0:
            user.id = new_username
        else:
            return "Error: There is already another user subscribed with this email address."
    else:
        pass
    user.surname = surname
    user.name = name
    user.birthdate = birthdate
    session.commit()
    session.close()
    return "OK"


def update_user_password(user_id, old_password, new_password, confirm_password):
    user = get_user_by_id(user_id)
    if old_password != user.password:
        return "Update failed: The current password you inserted is wrong!"
    if new_password != confirm_password:
        return "Update failed: New passwords do not match!"
    else:
        session = start_session()
        user = session.query(User).get(user_id)
        user.password = confirm_password
        session.commit()
        session.close()
        return "OK"

