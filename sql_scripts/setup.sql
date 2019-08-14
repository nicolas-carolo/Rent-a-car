CREATE DATABASE IF NOT EXISTS RENTACAR CHARACTER SET utf32;
CREATE USER IF NOT EXISTS 'rentacar-user'@'localhost' IDENTIFIED BY 'rent-a-car1';
GRANT ALTER, CREATE, DELETE, INSERT, REFERENCES, SELECT, UPDATE ON `RENTACAR`.* TO 'rentacar-user'@'localhost';

USE RENTACAR;

DROP TABLE IF EXISTS cars;
CREATE TABLE cars(
    id			      INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	brand    		  VARCHAR(30) NOT NULL,
	model  		      VARCHAR(50) NOT NULL,
	car_year          INT NOT NULL,
	plate             VARCHAR(10) NOT NULL,
	n_seats           INT NOT NULL,
	car_type          VARCHAR(30) NOT NULL,
	min_age           INT NOT NULL,
	engine            VARCHAR(10) NOT NULL,
	fuel              VARCHAR(20) NOT NULL,
	power             INT NOT NULL,
	transmission      VARCHAR(20) NOT NULL,
	photo_link        VARCHAR(200) NOT NULL,
	price             INT NOT NULL,
	preview           BOOLEAN
);

INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('BMW', 'X1 16d sDrive', 2016, 'FF001XB', 5, 'SUV', 23, '1.5', 'Diesel', 116, 'Manual', '/static/media/cars/bmw-x1-2016.jpg', 65, false );
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Mercedes', 'A180d', 2018, 'FP821DA', 5, 'Hatchback', 23, '1.5', 'Diesel', 116, 'Automatic', '/static/media/cars/mercedes-a180d.jpg', 65, true);
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Volkswagen', 'Tiguan', 2017, 'FN342BF', 5, 'SUV', 25, '2.0', 'Diesel', 150, 'Automatic', '/static/media/cars/vw-tiguan.jpg', 70, false );
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Peugeot', '3008', 2018, 'FP729HF', 5, 'SUV', 25, '2.0', 'Diesel', 150, 'Automatic', '/static/media/cars/peugeot-3008.jpg', 60, false );
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Ford', 'Fiesta', 2019, 'FV382LP', 5, 'Hatchback', 18, '1.0', 'Gasoline', 86, 'Manual', '/static/media/cars/ford-fiesta.jpg', 40, true);
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('BMW', '530d', 2012, 'EN161PV', 5, 'Station Wagon', 30, '3.0', 'Diesel', 245, 'Automatic', '/static/media/cars/bmw-530d.jpg', 90, true);
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('BMW', 'M5', 2018, 'FS086FH', 5, 'Sedan', 35, '4.4', 'Gasoline', 600, 'Automatic', '/static/media/cars/bmw-m5.jpg', 300, true);
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Fiat', 'Panda', 2013, 'ER453HS', 4, 'City Car', 18, '1.2', 'Gasoline', 69, 'Manual', '/static/media/cars/fiat-panda.jpg', 28, false );
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Lancia', 'Ypsilon', 2015, 'FA749LF', 4, 'City Car', 18, '1.2', 'Gasoline', 69, 'Manual', '/static/media/cars/lancia-y.jpg', 30, false );
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Mercedes', 'SLC200', 2018, 'FP271DT', 2, 'Roadster', 25, '2.0', 'Gasoline', 184, 'Automatic', '/static/media/cars/mercedes-slc200.jpg', 120, false );
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Porsche', 'Cayenne', 2012, 'EM383YR', 5, 'SUV', 30, '3.0', 'Diesel', 245, 'Automatic', '/static/media/cars/porsche-cayenne-2012.jpg', 100, false );
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Volkswagen', 'Passat Variant', 2017, 'FR764PP', 5, 'Station Wagon', 25, '2.0', 'Gasoline', 150, 'Manual', '/static/media/cars/vw-passat-variant.jpg', 70, false );
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Volkswagen', 'Polo', 2016, 'FG954ER', 5, 'Hatchback', 18, '1.4', 'Diesel', 75, 'Manual', '/static/media/cars/vw-polo.jpg', 35, false );


DROP TABLE IF EXISTS news;
CREATE TABLE news(
    id               INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    description      VARCHAR(1024) NOT NULL
);

INSERT INTO news(description) VALUES ('New BMW 320d Luxury available');
INSERT INTO news(description) VALUES ('New Mercedes A180d Automatic Premium available');
INSERT INTO news(description) VALUES ('From 15th to 17th on September we are going to be closed');


DROP TABLE IF EXISTS car_reservations;
CREATE TABLE car_reservations(
    id_reservation   INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_car           INT NOT NULL,
    id_user          VARCHAR(100) NOT NULL,
    date_from        DATE NOT NULL,
    date_to          DATE NOT NULL
);

INSERT INTO car_reservations(id_car, id_user, date_from, date_to) VALUES (1, 'sebastian.vettel@pilot.com', '2019-08-09', '2019-08-13');
INSERT INTO car_reservations(id_car, id_user, date_from, date_to) VALUES (3, 'lewis.hamilton@pilot.com', '2019-07-30', '2019-08-04');
INSERT INTO car_reservations(id_car, id_user, date_from, date_to) VALUES (2, 'valtteri.bottas@pilot.com', '2019-08-15', '2019-08-15');
INSERT INTO car_reservations(id_car, id_user, date_from, date_to) VALUES (2, 'lewis.hamilton@pilot.com', '2019-09-01', '2019-09-07');
INSERT INTO car_reservations(id_car, id_user, date_from, date_to) VALUES (7, 'utente40@test.com', '2019-07-10', '2019-07-12');
INSERT INTO car_reservations(id_car, id_user, date_from, date_to) VALUES (8, 'utente40@test.com', '2019-08-01', '2019-09-30');
INSERT INTO car_reservations(id_car, id_user, date_from, date_to) VALUES (5, 'utente40@test.com', '2020-01-01', '2020-01-15');
INSERT INTO car_reservations(id_car, id_user, date_from, date_to) VALUES (10, 'utente30@test.com', '2019-09-05', '2019-09-05');


DROP TABLE IF EXISTS sessions;
CREATE TABLE sessions(
    id_session       VARCHAR(100) PRIMARY KEY NOT NULL,
    id_user          VARCHAR(100) NOT NULL
);


DROP TABLE IF EXISTS users;
CREATE TABLE users(
    id              VARCHAR(100) PRIMARY KEY NOT NULL,
    password        VARCHAR(100) NOT NULL,
    surname         VARCHAR(50) NOT NULL,
    name            VARCHAR(50) NOT NULL,
    birthdate       DATE NOT NULL,
    is_admin           BOOLEAN
);

INSERT INTO users(id, password, surname, name, birthdate, is_admin) VALUES ('admin@rentacar.it', 'qwerty', 'Nicolas', 'Carolo', '1996-01-01', true);
INSERT INTO users(id, password, surname, name, birthdate, is_admin) VALUES ('sebastian.vettel@pilot.com', 'ferrari1', 'Sebastian', 'Vettel', '1987-07-03', false);
INSERT INTO users(id, password, surname, name, birthdate, is_admin) VALUES ('lewis.hamilton@pilot.com', 'mercedes', 'Lewis', 'Hamilton', '1985-01-07', false);
INSERT INTO users(id, password, surname, name, birthdate, is_admin) VALUES ('charles.leclerc@pilot.com', 'ferrari2', 'Charles', 'Leclerc', '1997-10-16', false);
INSERT INTO users(id, password, surname, name, birthdate, is_admin) VALUES ('utente30@test.com', '123', 'Utente', 'Trenta', '1989-01-01', false);
INSERT INTO users(id, password, surname, name, birthdate, is_admin) VALUES ('utente40@test.com', '456', 'Utente', 'Quaranta', '1979-01-01', false);


