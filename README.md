# Rent a Car

**__Rent a Car__** is an example of web application developed
in Python using Flask as web framework, MySQL as DBMS and
SQLAlchemy as ORM.
I developed this web application during the course of
Multimedia Systems and Technologies.

## Minimum requirements

### Interpreter and software dependencies

* Python 3
* MySQL
* venv [optional]

### Requested packages

Install these packages using pip:
* flask
* sqlalchemy

## Installation

1. Install the minimum requirements
2. Create the database:
    1. Go to the directory of the project
    (where there is `app.py`)
    2. Run the command:
        * Linux: `$ mysql -u root -p < sql_scripts/setup.sql`
        * macOS: `$ /usr/local/mysql/bin/mysql -u root -p < sql_scripts/setup.sql`
        * Windows: `$ mysql -u root -p < sql_scripts\setup.sql`
3. Create a new Python Virtual Environment:
    * `$ python -m venv ./venv`
4. Activate the Virtual Environment:
    * Linux and macOS: `$ source venv/bin/activate`
    * Windows: `venv\Scripts\activate.bat`
5. Run the web application server:
    * `$ python app.py`