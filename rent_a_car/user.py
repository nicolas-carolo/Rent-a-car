from rent_a_car.db_manager.session_manager import start_session
from rent_a_car.db_manager.models import CarReservation, User, Car
from rent_a_car.db_manager.result_set import queryset2list
from rent_a_car.home import get_car_identified_by_id
from rent_a_car.rent import get_total_price
from rent_a_car.sign_up import is_blank_input, get_age
import datetime


def get_user_by_id(user_id):
    session = start_session()
    queryset = session.query(User).filter(User.id.__eq__(user_id))
    session.close()
    print(queryset2list(queryset).__len__())
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
    session.query(CarReservation).filter(CarReservation.id_user.__eq__(old_username)).update({CarReservation.id_user:new_username}, synchronize_session = False)
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


def get_user_reservations_list(user_id):
    session = start_session()
    queryset = session.query(CarReservation).filter(CarReservation.id_user.__eq__(user_id))
    reservations_list = queryset2list(queryset)
    return sorted(reservations_list, key=lambda reservation: reservation.date_from, reverse=True)


def get_cars_user_reservations_list(reservations_list):
    car_list = []
    for reservation in reservations_list:
        car_list.append(get_car_identified_by_id(reservation.id_car))
    return car_list


def get_total_prices_reservations_list(reservations_list):
    total_prices_list = []
    for reservation in reservations_list:
        car = get_car_identified_by_id(reservation.id_car)
        total_prices_list.append(get_total_price(car.price, str(reservation.date_from), str(reservation.date_to)))
    return total_prices_list


def get_reservations_status_list(reservations_list):
    status_list = []
    today = datetime.datetime.today().date()
    for reservation in reservations_list:
        if reservation.date_from > today:
            status = 'Reserved'
        elif reservation.date_from <= today <= reservation.date_to:
            status = 'In progress'
        else:
            status = 'Completed'
        status_list.append(status)
    return status_list


def get_reservation_identified_by_id(reservation_id):
    session = start_session()
    reservation = session.query(CarReservation).get(reservation_id)
    session.close()
    return reservation


def is_reservation_of_the_user(reservation_id, user_id):
    reservations_list = get_user_reservations_list(user_id)
    reservations_id_list = []
    for reservation in reservations_list:
        reservations_id_list.append(str(reservation.id_reservation))
    if reservation_id in reservations_id_list:
        return True
    else:
        return False


def delete_reservation(reservation_id):
    session = start_session()
    session.query(CarReservation).filter(CarReservation.id_reservation.__eq__(reservation_id)).delete()
    session.commit()
    session.close()


def delete_user(user_id):
    session = start_session()
    session.query(User).filter(User.id.__eq__(user_id)).delete()
    session.commit()
    session.close()
    delete_all_user_reservations(user_id)


def delete_all_user_reservations(user_id):
    session = start_session()
    session.query(CarReservation).filter(CarReservation.id_user.__eq__(user_id)).delete()
    session.commit()
    session.close()


def is_admin_user(user_id):
    user = get_user_by_id(user_id)
    if user.is_admin:
        return True
    else:
        return False
