CREATE DATABASE IF NOT EXISTS RENTACAR CHARACTER SET utf32;
CREATE USER IF NOT EXISTS 'rentacar-user'@'localhost' IDENTIFIED BY 'rent-a-car1';
GRANT ALTER, CREATE, DELETE, INSERT, REFERENCES, SELECT, UPDATE ON `RENTACAR`.* TO 'rentacar-user'@'localhost';

USE RENTACAR;

DROP TABLE IF EXISTS cars;
CREATE TABLE cars(
    id			          INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	  brand    		      VARCHAR(30) NOT NULL,
	  model  		        VARCHAR(50) NOT NULL,
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

INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('BMW', 'X1 16d sDrive', 2016, 'FF001XB', 5, 'SUV', '23', '1.5', 'Diesel', 116, 'Manual', '/static/media/cars/bmw-x1-2016.jpg', 65, true);
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Mercedes', 'A180d Premium', 2018, 'FP821DA', 5, 'Hatchback', '23', '1.5', 'Diesel', 116, 'Automatic', '/static/media/cars/mercedes-a180d.jpg', 65, true);
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Volkswagen', 'Tiguan Sport', 2017, 'FN342BF', 5, 'SUV', '25', '2.0', 'Diesel', 150, 'Automatic', '/static/media/cars/vw-tiguan.jpg', 70, true);
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Peugeot', '3008 GT-Line', 2018, 'FP729HF', 5, 'SUV', '25', '2.0', 'Diesel', 150, 'Automatic', '/static/media/cars/peugeot-3008.jpg', 60, true);


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


DROP TABLE IF EXISTS sessions;
CREATE TABLE sessions(
    id_session       VARCHAR(100) PRIMARY KEY NOT NULL,
    id_user          VARCHAR(100) NOT NULL
);


DROP TABLE IF EXISTS users;
CREATE TABLE users(
    id              VARCHAR(100) PRIMARY KEY NOT NULL,
    password        VARCHAR(100) NOT NULL,
    age             INT NOT NULL
);

INSERT INTO users(id, password, age) VALUES ('sebastian.vettel@pilot.com', 'ferrari1', 32);
INSERT INTO users(id, password, age) VALUES ('lewis.hamilton@pilot.com', 'mercedes', 34);
INSERT INTO users(id, password, age) VALUES ('charles.leclerc@pilot.com', 'ferrari2', 21);
INSERT INTO users(id, password, age) VALUES ('utente30@test.com', '123', 30);


