from flask import Flask, render_template
from db_manager.session_manager import start_session
from db_manager.models import Car
from db_manager.result_set import queryset2list

app = Flask(__name__)


@app.route('/')
def home():
    session = start_session()
    queryset = session.query(Car)
    for car in queryset:
        print(car.brand)
    cars_list = queryset2list(queryset)
    session.close()
    return render_template('home.html', cars_list=cars_list)


if __name__ == '__main__':
    app.run()
