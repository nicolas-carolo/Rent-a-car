CREATE DATABASE IF NOT EXISTS RENTACAR CHARACTER SET utf32;
CREATE USER IF NOT EXISTS 'rentacar-user'@'localhost' IDENTIFIED BY 'rent-a-car1';
GRANT ALTER, CREATE, DELETE, INSERT, REFERENCES, SELECT, UPDATE ON `RENTACAR`.* TO 'rentacar-user'@'localhost';

USE RENTACAR;

DROP TABLE IF EXISTS cars;
CREATE TABLE cars(
  id					      INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
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
	photo_link        VARCHAR(200) NOT NULL,
	price             INT NOT NULL
);

INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, photo_link, price) VALUES ('BMW', 'X1 16d sDrive', 2016, 'FF001XB', 5, 'SUV', '23', '1.5', 'Diesel', 116, '/static/media/cars/bmw-x1-2016.jpg', 65);
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, photo_link, price) VALUES ('Mercedes', 'A180d Premium', 2018, 'FP821DA', 5, 'Hatchback', '23', '1.5', 'Diesel', 116, '/static/media/cars/mercedes-a180d.jpg', 65);
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, photo_link, price) VALUES ('Volkswagen', 'Tiguan Sport', 2017, 'FN342BF', 5, 'SUV', '25', '2.0', 'Diesel', 150, '/static/media/cars/vw-tiguan.jpg', 70);
INSERT INTO cars(brand, model, car_year, plate, n_seats, car_type, min_age, engine, fuel, power, photo_link, price) VALUES ('Peugeot', '3008 GT-Line', 2018, 'FP729HF', 5, 'SUV', '25', '2.0', 'Diesel', 150, '/static/media/cars/peugeot-3008.jpg', 60);