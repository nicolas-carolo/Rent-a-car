from flask import Flask, render_template, request
from rent_a_car.home import get_cars_preview, get_news_list, get_car_identified_by_id

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


if __name__ == '__main__':
    app.run()
