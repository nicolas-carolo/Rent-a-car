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

INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('BMW', 'X1 16d sDrive', 2016, 'FF001XB', 5, 'SUV', '23', '1.5', 'Diesel', 116, 'Manual', '/static/media/cars/bmw-x1-2016.jpg', 65, true);
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Mercedes', 'A180d Premium', 2018, 'FP821DA', 5, 'Hatchback', '23', '1.5', 'Diesel', 116, 'Automatic', '/static/media/cars/mercedes-a180d.jpg', 65, true);
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Volkswagen', 'Tiguan Sport', 2017, 'FN342BF', 5, 'SUV', '25', '2.0', 'Diesel', 150, 'Automatic', '/static/media/cars/vw-tiguan.jpg', 70, true);
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, transmission, photo_link, price, preview) VALUES ('Peugeot', '3008 GT-Line', 2018, 'FP729HF', 5, 'SUV', '25', '2.0', 'Diesel', 150, 'Automatic', '/static/media/cars/peugeot-3008.jpg', 60, true);


DROP TABLE IF EXISTS news;
CREATE TABLE news(
  id					      INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	description       VARCHAR(1024) NOT NULL
);

INSERT INTO news(description) VALUES ('New BMW 320d Luxury available');
INSERT INTO news(description) VALUES ('New Mercedes A180d Automatic Premium available');
INSERT INTO news(description) VALUES ('From 15th to 17th on September we are going to be closed');