from flask import Flask, render_template, request
from rent_a_car.home import get_cars_preview, get_news_list, get_car_identified_by_id
from rent_a_car.car_details import is_car_available_in_the_selected_period, get_total_price, are_dates_valid

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list())


@app.route('/cars')
def cars():
    return render_template('cars.html')


@app.route('/car_details', methods=['GET'])
def car_details():
    id = request.args.get('id', None)
    car = get_car_identified_by_id(id)
    return render_template('car_details.html', car=car)


@app.route('/check_availability', methods=['POST', 'GET'])
def check_car_availability():
    if request.method == 'POST':
        car_id = request.form['car-id']
        car = get_car_identified_by_id(car_id)
        date_from = request.form['date-from']
        date_to = request.form['date-to']
        if not are_dates_valid(date_from, date_to):
            return render_template('car_details.html', car=car, error="Please insert a valid date interval!")
        if is_car_available_in_the_selected_period(date_from, date_to, car_id):
            print('isAvailable', True)
            return render_template('car_details.html', car=car, is_available=True,
                                   total_price=get_total_price(car.price, date_from, date_to), show_confirm_div=True,
                                   date_from=date_from, date_to=date_to)
        else:
            print('isAvailable', False)
            return render_template('car_details.html', car=car, is_available=False, show_confirm_div=True,
                                   date_from=date_from, date_to=date_to)
    else:
        return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list())


if __name__ == '__main__':
    app.run()
