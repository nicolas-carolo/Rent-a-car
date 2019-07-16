from flask import Flask, render_template
from rent_a_car.home import get_cars_preview, get_news_list

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', cars_list=get_cars_preview(), news_list=get_news_list())


if __name__ == '__main__':
    app.run()
