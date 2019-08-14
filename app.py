from flask import Flask, render_template, request
from rent_a_car.home import get_cars_preview, get_news_list, get_car_identified_by_id
from rent_a_car.rent import is_car_available_in_the_selected_period, get_total_price, are_dates_valid,\
    save_car_reservation, has_user_age_requirement
from rent_a_car.authentication import authenticate as check_credentials, generate_session, delete_session,\
    check_authentication, get_user_by_session_id, edit_session
from rent_a_car.sign_up import create_account
from rent_a_car.cars_showcase import get_cars_list, get_current_year, get_car_brands_list, get_car_types_list,\
    get_car_n_seats_list, get_fuel_list, get_min_car_power_value, get_max_car_power_value, get_oldest_car_age,\
    get_max_car_price_per_day, get_min_car_price_per_day, filter_cars_by_user_parameters
from rent_a_car.user import get_user_by_id, edit_user_info, update_user_password, get_user_reservations_list,\
    get_cars_user_reservations_list, get_total_prices_reservations_list, get_reservations_status_list,\
    get_reservation_identified_by_id, is_reservation_of_the_user, delete_reservation, delete_user, is_admin_user
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    if check_authentication(session_id, user_id):
        return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), user=user_id,
                               session_id=session_id, authjs=True, preview_length=get_cars_preview().__len__())
    else:
        return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=True,
                               preview_length=get_cars_preview().__len__(), del_session_cookie=True)


@app.route('/cars')
def cars():
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    cars_list = get_cars_list()
    current_year = get_current_year()
    brands_list = get_car_brands_list()
    car_types_list = get_car_types_list()
    car_n_seats_list = get_car_n_seats_list()
    fuel_list = get_fuel_list()
    min_power = get_min_car_power_value()
    max_power = get_max_car_power_value()
    oldest_car_age_value = get_oldest_car_age()
    min_price = get_min_car_price_per_day()
    max_price = get_max_car_price_per_day()
    today = datetime.date.today()
    if check_authentication(session_id, user_id):
        return render_template('cars.html', user=user_id, session_id=session_id, cars_list=cars_list,
                               n_cars=cars_list.__len__(), current_year=current_year, brands_list=brands_list,
                               car_types_list=car_types_list, car_n_seats_list=car_n_seats_list, fuel_list=fuel_list,
                               min_power=min_power, max_power=max_power, oldest_car_age_value=oldest_car_age_value,
                               min_price=min_price, max_price=max_price, today=today)
    else:
        return render_template('cars.html',  cars_list=cars_list, n_cars=cars_list.__len__(), current_year=current_year,
                               brands_list=brands_list, car_types_list=car_types_list,
                               car_n_seats_list=car_n_seats_list, fuel_list=fuel_list, min_power=min_power,
                               max_power=max_power, oldest_car_age_value=oldest_car_age_value, min_price=min_price,
                               max_price=max_price, today=today)


@app.route('/car_details', methods=['GET'])
def car_details():
    car_id = request.args.get('car-id', None)
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    car = get_car_identified_by_id(car_id)
    today = datetime.date.today()
    if check_authentication(session_id, user_id):
        return render_template('car_details.html', car=car, user=user_id, session_id=session_id, today=today)
    else:
        return render_template('car_details.html', car=car, today=today)


@app.route('/check_availability', methods=['POST', 'GET'])
def check_car_availability():
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    today = datetime.date.today()
    if request.method == 'POST':
        car_id = request.form['car-id']
        car = get_car_identified_by_id(car_id)
        date_from = request.form['date-from']
        date_to = request.form['date-to']
        if not are_dates_valid(date_from, date_to):
            if check_authentication(session_id, user_id):
                return render_template('car_details.html', car=car, error="Please insert a valid date interval!", user=user_id, session_id=session_id, today=today)
            else:
                return render_template('car_details.html', car=car, error="Please insert a valid date interval!", today=today)
        if is_car_available_in_the_selected_period(date_from, date_to, car_id):
            if check_authentication(session_id, user_id):
                return render_template('car_details.html', car=car, is_available=True,
                                       total_price=get_total_price(car.price, date_from, date_to), show_confirm_div=True,
                                       date_from=date_from, date_to=date_to, user=user_id, session_id=session_id, today=today)
            else:
                return render_template('car_details.html', car=car, is_available=True,
                                       total_price=get_total_price(car.price, date_from, date_to),
                                       show_confirm_div=True,
                                       date_from=date_from, date_to=date_to, today=today)
        else:
            if check_authentication(session_id, user_id):
                return render_template('car_details.html', car=car, is_available=False, show_confirm_div=True,
                                       date_from=date_from, date_to=date_to, user=user_id, session_id=session_id, today=today)
            else:
                return render_template('car_details.html', car=car, is_available=False, show_confirm_div=True,
                                       date_from=date_from, date_to=date_to, today=today)
    else:
        if check_authentication(session_id, user_id):
            return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), user=user_id,
                                   session_id=session_id, authjs=False, preview_length=get_cars_preview().__len__())
        else:
            return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=False,
                                   preview_length=get_cars_preview().__len__(), del_session_cookie=True)


@app.route('/login')
def login():
    template = request.args.get('back', None)
    car_id = request.args.get('car-id', None)
    return render_template('login.html', template=template, car_id=car_id)


@app.route('/auth', methods=['POST', 'GET'])
def authenticate():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        template = request.form['backto']
        car_id = request.form['car-id']
        if check_credentials(username, password):
            return after_auth_redirect(template, car_id, username)
        else:
            return render_template('login.html', error="Bad credentials!")


@app.route('/logout')
def logout():
    session_id = request.args.get('session-id', None)
    delete_session(session_id)
    return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=False, preview_length=get_cars_preview().__len__())


@app.route('/auth_session_id', methods=['POST', 'GET'])
def authenticate_by_session_id():
    session_id = request.args.get('session-id', None)
    user_id = get_user_by_session_id(session_id)
    if check_authentication(session_id,user_id) and user_id is not None:
        return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), user=user_id,
                               session_id=session_id, authjs=False, preview_length=get_cars_preview().__len__())
    else:
        return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=False,
                               preview_length=get_cars_preview().__len__(), del_session_cookie=True)


def after_auth_redirect(template, car_id, username):
    session_id = generate_session(username)
    current_year = get_current_year()
    today = datetime.date.today()
    if template == "cars.html":
        return render_template('cars.html', user=username, session_id=session_id, current_year=current_year,
                               oldest_car_age_value=get_oldest_car_age(), n_cars=get_cars_list().__len__(),
                               cars_list=get_cars_list(), today=today)
    elif template == "car_details.html":
        car = get_car_identified_by_id(car_id)
        return render_template('car_details.html', car=car, user=username, session_id=session_id, today=today)
    else:
        return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), user=username, session_id=session_id, authjs=False, preview_length=get_cars_preview().__len__())


@app.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')


@app.route('/subscribe', methods=['POST', 'GET'])
def subscribe():
    if request.method == 'POST':
        surname = request.form['surname']
        name = request.form['name']
        birthdate = request.form['birthdate']
        username = request.form['username']
        password = request.form['password']
        retype_password = request.form['retype-password']
        is_new_user_valid = create_account(name, surname, birthdate, username, password, retype_password)
        if is_new_user_valid == "OK":
            session_id = generate_session(username)
            return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), user=username,
                                   session_id=session_id, authjs=False, user_added_correctly=True, preview_length=get_cars_preview().__len__())
        else:
            return render_template('sign_up.html', subscription_error=is_new_user_valid)


@app.route('/confirm_car_reservation', methods=['POST', 'GET'])
def confirm_car_reservation():
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    today = datetime.date.today()
    if request.method == 'POST':
        car_id = request.form['hidden-car-id']
        car = get_car_identified_by_id(car_id)
        date_from = request.form['hidden-date-from']
        date_to = request.form['hidden-date-to']
        if not are_dates_valid(date_from, date_to):
            if check_authentication(session_id, user_id):
                return render_template('car_details.html', car=car, error="Please insert a valid date interval!",
                                       user=user_id, session_id=session_id, today=today)
            else:
                return render_template('car_details.html', car=car, error="Please insert a valid date interval!", today=today)
        if is_car_available_in_the_selected_period(date_from, date_to, car_id):
            if check_authentication(session_id, user_id):
                if has_user_age_requirement(user_id, car_id):
                    reservation_id = save_car_reservation(car_id, user_id, date_from, date_to)
                    return render_template('car_reservation_details.html', user=user_id, session_id=session_id,
                                           reservation_id=reservation_id, car=car, date_from=date_from, date_to=date_to,
                                           total_price=get_total_price(car.price, date_from, date_to))
                else:
                    error_msg = "The reservation has failed because you are not at least " + str(car.min_age) +\
                                " years old!"
                    return render_template('car_details.html', user=user_id, session_id=session_id,
                                           error=error_msg, car=car, today=today)
            else:
                return render_template('car_details.html', car=car,
                                       error="You need to be authenticated in order to complete this action!", today=today)
        else:
            if check_authentication(session_id, user_id):
                return render_template('car_details.html', car=car, is_available=False, show_confirm_div=True,
                                       date_from=date_from, date_to=date_to, user=user_id, session_id=session_id, today=today)
            else:
                return render_template('car_details.html', car=car, is_available=False, show_confirm_div=True,
                                       date_from=date_from, date_to=date_to, today=today)
    else:
        if check_authentication(session_id, user_id):
            return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), user=user_id,
                                   session_id=session_id, authjs=False, preview_length=get_cars_preview().__len__())
        else:
            return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=False,
                                   preview_length=get_cars_preview().__len__(), del_session_cookie=True)


@app.route('/filter_cars', methods=['POST', 'GET'])
def filter_cars():
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    current_year = get_current_year()
    brands_list = get_car_brands_list()
    car_types_list = get_car_types_list()
    car_n_seats_list = get_car_n_seats_list()
    fuel_list = get_fuel_list()
    min_power = get_min_car_power_value()
    max_power = get_max_car_power_value()
    oldest_car_age_value = get_oldest_car_age()
    min_price = get_min_car_price_per_day()
    max_price = get_max_car_price_per_day()
    today = datetime.date.today()

    if request.method == 'POST':
        brand_filter = request.form['car-brand']
        type_filter = request.form['car-type']
        n_seats_filter = request.form['n-seats']
        min_power_filter = request.form['car-min-power']
        max_power_filter = request.form['car-max-power']
        fuel_filter = request.form['car-fuel']
        transmission_filter = request.form['car-transmission']
        car_year_from_filter = request.form['car-year-from']
        car_year_to_filter = request.form['car-year-to']
        driver_age_filter = request.form['driver-age']
        min_price_day_filter = request.form['min-price-day']
        max_price_day_filter = request.form['max-price-day']
        rent_date_from_filter = request.form['rent-date-from']
        rent_date_to_filter = request.form['rent-date-to']
        cars_list = filter_cars_by_user_parameters(brand_filter, type_filter, n_seats_filter, min_power_filter,
                                                   max_power_filter, fuel_filter, transmission_filter,
                                                   car_year_from_filter, car_year_to_filter, driver_age_filter,
                                                   min_price_day_filter, max_price_day_filter, rent_date_from_filter,
                                                   rent_date_to_filter)
        try:
            driver_age_filter = int(driver_age_filter)
        except ValueError:
            pass

        if check_authentication(session_id, user_id):
            return render_template('cars.html', user=user_id, session_id=session_id, cars_list=cars_list,
                                   n_cars=cars_list.__len__(), current_year=int(current_year), brands_list=brands_list,
                                   car_types_list=car_types_list, car_n_seats_list=car_n_seats_list,
                                   fuel_list=fuel_list, min_power=min_power, max_power=max_power,
                                   oldest_car_age_value=oldest_car_age_value, min_price=min_price, max_price=max_price,
                                   brand_filter=brand_filter, type_filter=type_filter,
                                   n_seats_filter=n_seats_filter, min_power_filter=min_power_filter,
                                   max_power_filter=max_power_filter, fuel_filter=fuel_filter,
                                   transmission_filter=transmission_filter,
                                   car_year_from_filter=int(car_year_from_filter),
                                   car_year_to_filter=int(car_year_to_filter), driver_age_filter=driver_age_filter,
                                   min_price_day_filter=min_price_day_filter, max_price_day_filter=max_price_day_filter,
                                   rent_date_from_filter=rent_date_from_filter, rent_date_to_filter=rent_date_to_filter,
                                   today=today)
        else:
            return render_template('cars.html',  cars_list=cars_list, n_cars=cars_list.__len__(),
                                   current_year=int(current_year), brands_list=brands_list,
                                   car_types_list=car_types_list, car_n_seats_list=car_n_seats_list,
                                   fuel_list=fuel_list, min_power=min_power, max_power=max_power,
                                   oldest_car_age_value=oldest_car_age_value, min_price=min_price, max_price=max_price,
                                   brand_filter=brand_filter, type_filter=type_filter,
                                   n_seats_filter=n_seats_filter, min_power_filter=min_power_filter,
                                   max_power_filter=max_power_filter, fuel_filter=fuel_filter,
                                   transmission_filter=transmission_filter,
                                   car_year_from_filter=int(car_year_from_filter),
                                   car_year_to_filter=int(car_year_to_filter), driver_age_filter=driver_age_filter,
                                   min_price_day_filter=min_price_day_filter, max_price_day_filter=max_price_day_filter,
                                   rent_date_from_filter=rent_date_from_filter, rent_date_to_filter=rent_date_to_filter,
                                   today=today)
    else:
        cars_list = get_cars_list()
        if check_authentication(session_id, user_id):
            return render_template('cars.html', user=user_id, session_id=session_id, cars_list=cars_list,
                                   n_cars=cars_list.__len__(), current_year=current_year, brands_list=brands_list,
                                   car_types_list=car_types_list, car_n_seats_list=car_n_seats_list,
                                   fuel_list=fuel_list, min_power=min_power, max_power=max_power,
                                   oldest_car_age_value=oldest_car_age_value, min_price=min_price,
                                   max_price=max_price, today=today)
        else:
            return render_template('cars.html',  cars_list=cars_list, n_cars=cars_list.__len__(),
                                   current_year=current_year, brands_list=brands_list, car_types_list=car_types_list,
                                   car_n_seats_list=car_n_seats_list, fuel_list=fuel_list, min_power=min_power,
                                   max_power=max_power, oldest_car_age_value=oldest_car_age_value, min_price=min_price,
                                   max_price=max_price, today=today)


@app.route('/user_area')
def user_area():
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    edit = request.args.get('edit', None)
    today = datetime.date.today()
    reservations_list = get_user_reservations_list(user_id)
    total_prices_list = get_total_prices_reservations_list(reservations_list)
    cars_reservations_list = get_cars_user_reservations_list(reservations_list)
    reservations_status_list = get_reservations_status_list(reservations_list)
    if edit == "true":
        edit_mode = True
    else:
        edit_mode = False
    user = get_user_by_id(user_id)
    if check_authentication(session_id, user_id):
        if is_admin_user(user_id):
            return render_template('admin_area.html', user=user_id, session_id=session_id)
        else:
            return render_template('user_area.html', user=user_id, session_id=session_id, edit_mode=edit_mode,
                                   surname=user.surname, name=user.name, birthdate=user.birthdate, today=today,
                                   reservations_list=reservations_list, cars_reservations_list=cars_reservations_list,
                                   total_prices_list=total_prices_list, reservations_status_list=reservations_status_list)
    else:
        return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=False,
                               preview_length=get_cars_preview().__len__(), del_session_cookie=True)


@app.route('/edit_user_info', methods=['POST', 'GET'])
def edit_user_information():
    session_id = request.args.get('session-id', None)
    old_username = request.args.get('user-id', None)
    user = get_user_by_id(old_username)
    if request.method == 'POST':
        surname = request.form['surname']
        name = request.form['name']
        birthdate = request.form['birthdate']
        new_username = request.form['username']
        today = datetime.date.today()
        reservations_list = get_user_reservations_list(old_username)
        total_prices_list = get_total_prices_reservations_list(reservations_list)
        cars_reservations_list = get_cars_user_reservations_list(reservations_list)
        reservations_status_list = get_reservations_status_list(reservations_list)
        if check_authentication(session_id, old_username):
            are_changes_valid = edit_user_info(name, surname, birthdate, old_username, new_username)
        else:
            return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=False,
                                   preview_length=get_cars_preview().__len__(), del_session_cookie=True)
        if are_changes_valid == "OK":
            edit_session(session_id, new_username)
            return render_template('user_area.html', user=new_username, session_id=session_id, edit_mode=False,
                                   surname=surname, name=name, birthdate=birthdate, today=today,
                                   reservations_list=reservations_list, cars_reservations_list=cars_reservations_list,
                                   total_prices_list=total_prices_list,
                                   reservations_status_list=reservations_status_list)
        else:
            return render_template('user_area.html', user=user.id, session_id=session_id, edit_mode=True,
                                   surname=user.surname, name=user.name, birthdate=user.birthdate,
                                   feedback_msg=are_changes_valid, today=today,
                                   reservations_list=reservations_list, cars_reservations_list=cars_reservations_list,
                                   total_prices_list=total_prices_list,
                                   reservations_status_list=reservations_status_list)


@app.route('/change_pwd', methods=['POST', 'GET'])
def change_user_password():
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    user = get_user_by_id(user_id)
    if request.method == 'POST':
        old_password = request.form['old-password']
        new_password = request.form['new-password']
        confirm_password = request.form['confirm-password']
        today = datetime.date.today()
        reservations_list = get_user_reservations_list(user_id)
        total_prices_list = get_total_prices_reservations_list(reservations_list)
        cars_reservations_list = get_cars_user_reservations_list(reservations_list)
        reservations_status_list = get_reservations_status_list(reservations_list)
        if check_authentication(session_id, user_id):
            is_password_updated = update_user_password(user_id, old_password, new_password, confirm_password)
        else:
            return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=False,
                                   preview_length=get_cars_preview().__len__(), del_session_cookie=True)
        if is_password_updated == "OK":
            return render_template('user_area.html', user=user.id, session_id=session_id, edit_mode=False,
                                   surname=user.surname, name=user.name, birthdate=user.birthdate,
                                   feedback_msg="Password successfully updated!", today=today,
                                   reservations_list=reservations_list, cars_reservations_list=cars_reservations_list,
                                   total_prices_list=total_prices_list,
                                   reservations_status_list=reservations_status_list)
        else:
            return render_template('user_area.html', user=user.id, session_id=session_id, edit_mode=False,
                                   surname=user.surname, name=user.name, birthdate=user.birthdate,
                                   feedback_msg=is_password_updated, today=today,
                                   reservations_list=reservations_list, cars_reservations_list=cars_reservations_list,
                                   total_prices_list=total_prices_list,
                                   reservations_status_list=reservations_status_list)


@app.route('/reservation_details')
def reservation_details():
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    reservation_id = request.args.get('reservation-id', None)
    reservation = get_reservation_identified_by_id(reservation_id)
    car = get_car_identified_by_id(reservation.id_car)
    date_from = str(reservation.date_from)
    date_to = str(reservation.date_to)
    total_price = get_total_price(car.price, date_from, date_to)
    if check_authentication(session_id, user_id) and is_reservation_of_the_user(reservation_id, user_id):
        return render_template('car_reservation_details.html', user=user_id, session_id=session_id, car=car,
                               reservation_id=reservation_id, date_from=date_from,
                               date_to=date_to, total_price=total_price)
    else:
        return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=False,
                               preview_length=get_cars_preview().__len__(), del_session_cookie=True)


@app.route('/delete_reservation')
def detele_car_reservation():
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    reservation_id = request.args.get('reservation-id', None)
    today = datetime.date.today()
    if check_authentication(session_id, user_id) and is_reservation_of_the_user(reservation_id, user_id):
        delete_reservation(reservation_id)
        reservations_list = get_user_reservations_list(user_id)
        total_prices_list = get_total_prices_reservations_list(reservations_list)
        cars_reservations_list = get_cars_user_reservations_list(reservations_list)
        reservations_status_list = get_reservations_status_list(reservations_list)
        user = get_user_by_id(user_id)
        return render_template('user_area.html', user=user_id, session_id=session_id, edit_mode=False,
                               surname=user.surname, name=user.name, birthdate=user.birthdate, today=today,
                               reservations_list=reservations_list, cars_reservations_list=cars_reservations_list,
                               total_prices_list=total_prices_list, reservations_status_list=reservations_status_list)
    else:
        return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=False,
                               preview_length=get_cars_preview().__len__(), del_session_cookie=True)


@app.route('/delete_user')
def detele_account():
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    delete_user(user_id)
    delete_session(session_id)
    return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=False,
                           preview_length=get_cars_preview().__len__(), user_deleted=user_id)


if __name__ == '__main__':
    app.run()
