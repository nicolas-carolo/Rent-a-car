from flask import Flask, render_template, request
from rent_a_car.home import get_cars_preview, get_news_list, get_car_identified_by_id
from rent_a_car.car_details import is_car_available_in_the_selected_period, get_total_price, are_dates_valid, save_car_reservation
from rent_a_car.authentication import authenticate as check_credentials, generate_session, delete_session,\
    check_authentication, get_user_by_session_id
from rent_a_car.sign_up import create_account

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
                               preview_length=get_cars_preview().__len__())


@app.route('/cars')
def cars():
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    if check_authentication(session_id, user_id):
        return render_template('cars.html', user=user_id, session_id=session_id)
    else:
        return render_template('cars.html')


@app.route('/car_details', methods=['GET'])
def car_details():
    car_id = request.args.get('car-id', None)
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    car = get_car_identified_by_id(car_id)
    if check_authentication(session_id, user_id):
        return render_template('car_details.html', car=car, user=user_id, session_id=session_id)
    else:
        return render_template('car_details.html', car=car)


@app.route('/check_availability', methods=['POST', 'GET'])
def check_car_availability():
    session_id = request.args.get('session-id', None)
    user_id = request.args.get('user-id', None)
    if request.method == 'POST':
        car_id = request.form['car-id']
        car = get_car_identified_by_id(car_id)
        date_from = request.form['date-from']
        date_to = request.form['date-to']
        if not are_dates_valid(date_from, date_to):
            if check_authentication(session_id, user_id):
                return render_template('car_details.html', car=car, error="Please insert a valid date interval!", user=user_id, session_id=session_id)
            else:
                return render_template('car_details.html', car=car, error="Please insert a valid date interval!")
        if is_car_available_in_the_selected_period(date_from, date_to, car_id):
            if check_authentication(session_id, user_id):
                return render_template('car_details.html', car=car, is_available=True,
                                       total_price=get_total_price(car.price, date_from, date_to), show_confirm_div=True,
                                       date_from=date_from, date_to=date_to, user=user_id, session_id=session_id)
            else:
                return render_template('car_details.html', car=car, is_available=True,
                                       total_price=get_total_price(car.price, date_from, date_to),
                                       show_confirm_div=True,
                                       date_from=date_from, date_to=date_to)
        else:
            if check_authentication(session_id, user_id):
                return render_template('car_details.html', car=car, is_available=False, show_confirm_div=True,
                                       date_from=date_from, date_to=date_to, user=user_id, session_id=session_id)
            else:
                return render_template('car_details.html', car=car, is_available=False, show_confirm_div=True,
                                       date_from=date_from, date_to=date_to)
    else:
        if check_authentication(session_id, user_id):
            return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), user=user_id, session_id=session_id, authjs=False, preview_length=get_cars_preview().__len__())
        else:
            return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=False, preview_length=get_cars_preview().__len__())


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
        return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=False, preview_length=get_cars_preview().__len__())


def after_auth_redirect(template, car_id, username):
    session_id = generate_session(username)
    if template == "cars.html":
        return render_template('cars.html', user=username, session_id=session_id)
    elif template == "car_details.html":
        car = get_car_identified_by_id(car_id)
        return render_template('car_details.html', car=car, user=username, session_id=session_id)
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
    if request.method == 'POST':
        car_id = request.form['hidden-car-id']
        car = get_car_identified_by_id(car_id)
        date_from = request.form['hidden-date-from']
        date_to = request.form['hidden-date-to']
        if not are_dates_valid(date_from, date_to):
            if check_authentication(session_id, user_id):
                return render_template('car_details.html', car=car, error="Please insert a valid date interval!",
                                       user=user_id, session_id=session_id)
            else:
                return render_template('car_details.html', car=car, error="Please insert a valid date interval!")
        if is_car_available_in_the_selected_period(date_from, date_to, car_id):
            if check_authentication(session_id, user_id):
                reservation_id = save_car_reservation(car_id, user_id, date_from, date_to)
                return render_template('reservation_details.html', user=user_id, session_id=session_id,
                                       reservation_id=reservation_id)
            else:
                return render_template('car_details.html', car=car,
                                       error="the reservation has been canceled because you are not authenticated!")
        else:
            if check_authentication(session_id, user_id):
                return render_template('car_details.html', car=car, is_available=False, show_confirm_div=True,
                                       date_from=date_from, date_to=date_to, user=user_id, session_id=session_id)
            else:
                return render_template('car_details.html', car=car, is_available=False, show_confirm_div=True,
                                       date_from=date_from, date_to=date_to)
    else:
        if check_authentication(session_id, user_id):
            return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), user=user_id,
                                   session_id=session_id, authjs=False, preview_length=get_cars_preview().__len__())
        else:
            return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list(), authjs=False,
                                   preview_length=get_cars_preview().__len__())


if __name__ == '__main__':
    app.run()
