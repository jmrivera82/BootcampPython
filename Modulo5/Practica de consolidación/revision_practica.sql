CREATE DATABASE dvdrental;

CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    store_id INTEGER NOT NULL,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45)NOT NULL,
    email VARCHAR(80),
    address_id INTEGER NOT NULL,
    activebool BOOLEAN NOT NULL,
    create_update DATE DEFAULT now(),
    last_update DATE DEFAULT now(), 
    active integer
);

ALTER TABLE customer ALTER COLUMN activebool SET DEFAULT TRUE; 

CREATE TABLE actor (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    last_update DATE DEFAULT now()
);


CREATE TABLE category (
    category_id SERIAL PRIMARY KEY,
    name_category VARCHAR(45) NOT NULL, /*Se cambió valor de name a name_category por problema con palabra reservada?*/
    last_update DATE DEFAULT now()
);


CREATE TABLE film (
    film_id SERIAL PRIMARY KEY,
    title VARCHAR(45) NOT NULL,
    description VARCHAR(100) NOT NULL, 
    release_year INTEGER NOT NULL,
    language_id INTEGER NOT NULL,
    rental_duration INTEGER DEFAULT 3 NOT NULL,
    rental_rate NUMERIC(4,2) DEFAULT 4.99 NOT NULL,
    length_film INTEGER,
    replacement_cost NUMERIC(5,2) DEFAULT 19.99 NOT NULL,
    rating VARCHAR(2) DEFAULT 'G' NOT NULL,
    last_update DATE DEFAULT now(),
    special_features VARCHAR(45),
    fulltext_film VARCHAR(45) 
);


CREATE TABLE film_actor (
    actor_id INTEGER NOT NULL, 
    film_id INTEGER NOT NULL, 
    last_update DATE DEFAULT now()
);



CREATE TABLE film_category (
    film_id INTEGER NOT NULL, /*PK tabla film*/
    category_id smallint NOT NULL, /*PK tabla category*/
    last_update DATE DEFAULT now()
);


CREATE TABLE address (
    address_id SERIAL PRIMARY KEY,
    address VARCHAR(45) NOT NULL,
    address2 VARCHAR(45) NOT NULL,
    district VARCHAR(45) NOT NULL,
    city_id INTEGER NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    last_update DATE DEFAULT now()
);



CREATE TABLE city (
    city_id INTEGER PRIMARY KEY,
    city VARCHAR(45) NOT NULL,
    country_id INTEGER NOT NULL,
    last_update DATE DEFAULT now() 
);


CREATE TABLE country (
    country_id SERIAL PRIMARY KEY,
    country VARCHAR(45) NOT NULL,
    last_update DATE DEFAULT now()
);


CREATE TABLE inventory (
    inventory_id SERIAL PRIMARY KEY,
    film_id INTEGER NOT NULL,
    store_id INTEGER NOT NULL,
    last_update DATE DEFAULT now()
);


CREATE TABLE language (
    language_id SERIAL PRIMARY KEY,
    name_language VARCHAR(20) NOT NULL,
    last_update DATE DEFAULT now()
);



CREATE TABLE payment (
    payment_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    rental_id INTEGER NOT NULL,
    amount NUMERIC(5,2) NOT NULL,
    payment_date DATE DEFAULT Now()
);


CREATE TABLE rental (
    rental_id INTEGER PRIMARY KEY,
    rental_date DATE NOT NULL,
    inventory_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    return_date DATE NOT NULL,
    staff_id INTEGER NOT NULL,
    last_update DATE DEFAULT Now()
);

CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    address_id INTEGER NOT NULL,
    email VARCHAR(50),
    store_id INTEGER NOT NULL,
    active BOOLEAN DEFAULT true NOT NULL,
    username VARCHAR(16) NOT NULL,
    password VARCHAR(40),
    last_update DATE DEFAULT now()
);

CREATE TABLE store (
    store_id SERIAL PRIMARY KEY,
    manager_staff_id INTEGER NOT NULL,
    address_id INTEGER NOT NULL,
    last_update DATE DEFAULT now()
);

ALTER TABLE customer ADD CONSTRAINT customer_address_id_fk FOREIGN KEY (address_id) REFERENCES address(address_id);

ALTER TABLE address ADD CONSTRAINT fk_address_city FOREIGN KEY (city_id) REFERENCES city(city_id);

ALTER TABLE city ADD CONSTRAINT fk_city FOREIGN KEY (country_id) REFERENCES country(country_id);

ALTER TABLE inventory ADD CONSTRAINT inventory_film_id_fk FOREIGN KEY (film_id) REFERENCES film(film_id);

ALTER TABLE rental ADD CONSTRAINT rental_customer_id_fk FOREIGN KEY (customer_id) REFERENCES customer(customer_id);

ALTER TABLE rental ADD CONSTRAINT rental_inventory_id_fk FOREIGN KEY (inventory_id) REFERENCES inventory(inventory_id);

ALTER TABLE rental ADD CONSTRAINT rental_staff_id_fk FOREIGN KEY (staff_id) REFERENCES staff(staff_id);

ALTER TABLE staff ADD CONSTRAINT staff_address_id_fk FOREIGN KEY (address_id) REFERENCES address(address_id);

ALTER TABLE store ADD CONSTRAINT store_address_id_fk FOREIGN KEY (address_id) REFERENCES address(address_id);

ALTER TABLE store ADD CONSTRAINT store_manager_staff_id_fk FOREIGN KEY (manager_staff_id) REFERENCES staff(staff_id);

ALTER TABLE payment ADD CONSTRAINT payment_customer_id_fk FOREIGN KEY (customer_id) REFERENCES customer(customer_id);

ALTER TABLE payment ADD CONSTRAINT payment_rental_id_fk FOREIGN KEY (rental_id) REFERENCES rental(rental_id);

ALTER TABLE payment ADD CONSTRAINT payment_staff_id_fk FOREIGN KEY (staff_id) REFERENCES staff(staff_id);

ALTER TABLE film_category ADD CONSTRAINT film_category_film_id_fk FOREIGN KEY (film_id) REFERENCES film(film_id);

ALTER TABLE film_category ADD CONSTRAINT film_category_category_id_fk FOREIGN KEY (category_id) REFERENCES category(category_id);

ALTER TABLE film_actor ADD CONSTRAINT film_actor_film_id_fk FOREIGN KEY (film_id) REFERENCES film(film_id);

ALTER TABLE film_actor ADD CONSTRAINT film_actor_actor_id_fk FOREIGN KEY (actor_id) REFERENCES actor(actor_id);

ALTER TABLE film ADD CONSTRAINT film_language_id_fk FOREIGN KEY (language_id) REFERENCES language(language_id);


INSERT INTO customer (store_id,first_name,last_name,email,address_id,activebool,create_update,last_update,active) VALUES (1,'Mary','Smith','mary.smith@sakilacustomer.org',1,'True','2006-02-14','2013-05-26',1);
INSERT INTO customer (store_id,first_name,last_name,email,address_id,activebool,create_update,last_update,active) VALUES (1,'Patricia','Johnson','patricia.johnson@sakilacustomer.org',2,'True','2006-02-14','2013-05-26',1);
INSERT INTO customer (store_id,first_name,last_name,email,address_id,activebool,create_update,last_update,active) VALUES (1,'Linda','Williams','linda.williams@sakilacustomer.org',7,'True','2006-02-14','2013-05-21',1);
INSERT INTO customer (store_id,first_name,last_name,email,address_id,activebool,create_update,last_update,active) VALUES (2,'Barbara','Jones','barbara.jones@sakilacustomer.org',8,'True','2006-02-14','2013-05-26',1);
INSERT INTO customer (store_id,first_name,last_name,email,address_id,activebool,create_update,last_update,active) VALUES (2,'Jennifer','Davis','jennifer.davis@sakilacustomer.org',10,'True','2006-02-14','2013-05-26',1);

INSERT INTO actor (first_name,last_name,last_update) VALUES ('Penelope','Guiness','2013-05-26');
INSERT INTO actor (first_name,last_name,last_update) VALUES ('Nick','Wahlberg','2013-05-26');
INSERT INTO actor (first_name,last_name,last_update) VALUES ('Ed','Chase','2013-05-26');
INSERT INTO actor (first_name,last_name,last_update) VALUES ('Jennifer','Davis','2013-05-26');
INSERT INTO actor (first_name,last_name,last_update) VALUES ('Johnny','Lollobrigida','2013-05-26');

INSERT INTO category (name_category,last_update) VALUES ('Action','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Animation','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Children','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Classics','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Comedy','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Documentary','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Drama','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Family','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Family','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Foreign','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Games','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Horror','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Music','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('New','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Sci-Fi','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Sports','2006-02-15');
INSERT INTO category (name_category,last_update) VALUES ('Travel','2006-02-15');

INSERT INTO film (title,description,release_year,language_id,rental_duration,rental_rate,length_film,replacement_cost,rating,last_update,special_features,fulltext_film) Values ('Academy Dinosaur','A Epic Drama of a Feminist',2006,1,6,0.99,86,20.99,'PG','2013-05-26','Deleted Scenes','Behind the Scenes');
INSERT INTO film (title,description,release_year,language_id,rental_duration,rental_rate,length_film,replacement_cost,rating,last_update,special_features,fulltext_film) VALUES ('Ace Goldfinger','A Astounding Epistle of a Database Administrator',2006,1,3,4.99,48,12.99,'G','2013-05-26','Trailers','Deleted Scenes');
INSERT INTO film (title,description,release_year,language_id,rental_duration,rental_rate,length_film,replacement_cost,rating,last_update,special_features,fulltext_film) VALUES ('Army Flintstones','A Boring Saga of a Database Administrator',2006,1,4,0.99,148,22.99,'R','2013-05-26','Trailers','Commentaries');
INSERT INTO film (title,description,release_year,language_id,rental_duration,rental_rate,length_film,replacement_cost,rating,last_update,special_features,fulltext_film) VALUES ('Beethoven Exorcist','A Epic Display of a Pioneer And a Student',2007,1,6,0.99,151,26.99,'PG','2013-05-26','Commentaries','Behind the Scenes');
INSERT INTO film (title,description,release_year,language_id,rental_duration,rental_rate,length_film,replacement_cost,rating,last_update,special_features,fulltext_film) VALUES ('Cleopatra Devil','A Fanciful Documentary of a Crocodile',2006,1,6,0.99,150,26.99,'PG','2013-05-26','Trailers, Deleted Scenes','Behind the Scenes');
INSERT INTO film (title,description,release_year,language_id,rental_duration,rental_rate,length_film,replacement_cost,rating,last_update,special_features,fulltext_film) VALUES ('Chocolate Duck','A Unbelieveable Story of a Mad Scientist And a Technical Writer',2008,1,3,2.99,132,13.99,'R','2013-05-26','Trailers,Commentaries','Behind the Scenes');
INSERT INTO film (title,description,release_year,language_id,rental_duration,rental_rate,length_film,replacement_cost,rating,last_update,special_features,fulltext_film) VALUES ('Brooklyn Desert','A Beautiful Drama of a Dentist And a Composer',2010,1,7,4.99,161,21.99,'R','2013-05-26','Commentaries',' ');
INSERT INTO film (title,description,release_year,language_id,rental_duration,rental_rate,length_film,replacement_cost,rating,last_update,special_features,fulltext_film) VALUES ('Braveheart Human','A Insightful Story of a Dog And a Pastry Chef',2006,1,7,2.99,176,14.99,'PG','2013-05-26','Trailers','Deleted Scenes');
INSERT INTO film (title,description,release_year,language_id,rental_duration,rental_rate,length_film,replacement_cost,rating,last_update,special_features,fulltext_film) VALUES ('Bucket Brotherhood','A Amazing Display of a Girl And a Womanizer',2010,1,7,4.99,133,27.99,'PG','2013-05-26','Commentaries','Deleted Scenes');
INSERT INTO film (title,description,release_year,language_id,rental_duration,rental_rate,length_film,replacement_cost,rating,last_update,special_features,fulltext_film) VALUES ('American Circus','A Insightful Drama of a Girl And a Astronaut',2006,1,3,4.99,129,17.99,'R','2013-05-26','Commentaries','Behind the Scenes');


INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (1,1,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (1,2,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (1,3,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (1,4,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (1,5,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (2,1,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (2,2,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (2,2,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (2,3,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (2,4,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (3,1,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (3,2,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (3,3,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (4,3,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (5,3,'2006-02-15');
INSERT INTO film_actor (actor_id,film_id,last_update) VALUES (5,5,'2006-02-15');

INSERT INTO film_category (film_id, category_id, last_update) VALUES (1,1,'2006-02-15');
INSERT INTO film_category (film_id, category_id, last_update) VALUES (2,1,'2006-02-15');
INSERT INTO film_category (film_id, category_id, last_update) VALUES (3,2,'2006-02-15');
INSERT INTO film_category (film_id, category_id, last_update) VALUES (4,2,'2006-02-15');
INSERT INTO film_category (film_id, category_id, last_update) VALUES (5,3,'2006-02-15');
INSERT INTO film_category (film_id, category_id, last_update) VALUES (6,3,'2006-02-15');
INSERT INTO film_category (film_id, category_id, last_update) VALUES (7,3,'2006-02-15');
INSERT INTO film_category (film_id, category_id, last_update) VALUES (8,4,'2006-02-15');
INSERT INTO film_category (film_id, category_id, last_update) VALUES (9,5,'2006-02-15');
INSERT INTO film_category (film_id, category_id, last_update) VALUES (10,5,'2006-02-15');

INSERT INTO address (address,address2,district,city_id,postal_code,phone,last_update) VALUES ('47 MySakila Drive','47 MySakila Drive','Alberta',300,35200,'2222222233','2006-02-15');
INSERT INTO address (address,address2,district,city_id,postal_code,phone,last_update) VALUES ('28 MySQL Boulevard','28 MySQL Boulevard','QLD',576,35200,'11111111112','2006-02-15');
INSERT INTO address (address,address2,district,city_id,postal_code,phone,last_update) VALUES ('23 Workhaven Lane','23 Workhaven Lane','Alberta',300,35200,'14033335568','2006-02-15');
INSERT INTO address (address,address2,district,city_id,postal_code,phone,last_update) VALUES ('1411 Lillydale Drive','1411 Lillydale Drive','QLD',576,35200,'6172235589','2006-02-15');
INSERT INTO address (address,address2,district,city_id,postal_code,phone,last_update) VALUES ('333 Hanoi Way','1913 Hanoi Way','Nagasaki',463,35200,'28303384290','2006-02-15');
INSERT INTO address (address,address2,district,city_id,postal_code,phone,last_update) VALUES ('222 Hanoi Way','1914 Hanoi Way','Chayna',463,35200,'28303384290','2006-02-15');
INSERT INTO address (address,address2,district,city_id,postal_code,phone,last_update) VALUES ('11 Hanoi Way','1915 Hanoi Way','Tokio',463,35200,'28303384290','2006-02-15');

INSERT INTO city (city_id,city, country_id,last_update) VALUES (463,'Sasebo',1,'2006-02-15');
INSERT INTO city (city_id,city, country_id,last_update) VALUES (300,'Lethbridge',2,'2006-02-15');
INSERT INTO city (city_id,city, country_id,last_update) VALUES (576,'Woodridge',3,'2006-02-15');

INSERT INTO country (country,last_update) VALUES ('Chile','2006-02-15');
INSERT INTO country (country,last_update) VALUES ('Argentina','2006-02-15');
INSERT INTO country (country,last_update) VALUES ('Brazil','2006-02-15');
INSERT INTO country (country,last_update) VALUES ('China','2006-02-15');
INSERT INTO country (country,last_update) VALUES ('Japón','2006-02-15');
INSERT INTO country (country,last_update) VALUES ('United States','2006-02-15');
INSERT INTO country (country,last_update) VALUES ('United Kingdom','2006-02-15');
INSERT INTO country (country,last_update) VALUES ('Germany','2006-02-15');
INSERT INTO country (country,last_update) VALUES ('Italy','2006-02-15');
INSERT INTO country (country,last_update) VALUES ('Spain','2006-02-15');
INSERT INTO country (country,last_update) VALUES ('France','2006-02-15');
INSERT INTO country (country,last_update) VALUES ('Mexico','2006-02-15');
INSERT INTO country (country,last_update) VALUES ('South Africa','2006-02-15');

INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (2,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (2,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (2,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (2,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (3,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (3,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (3,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (4,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (4,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (4,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (4,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (5,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (5,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (5,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (1,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (2,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (2,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (2,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (2,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (3,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (3,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (3,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (4,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (4,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (4,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (4,2,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (5,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (5,1,'2006-02-15');
INSERT INTO inventory(film_id,store_id,last_update) VALUES (5,2,'2006-02-15');


INSERT INTO language (name_language,last_update) VALUES ('English','2006-02-15' );
INSERT INTO language (name_language,last_update) VALUES ('Italian','2006-02-15' );
INSERT INTO language (name_language,last_update) VALUES ('Japanese','2006-02-15' );
INSERT INTO language (name_language,last_update) VALUES ('Mandarin','2006-02-15' );
INSERT INTO language (name_language,last_update) VALUES ('French','2006-02-15' );
INSERT INTO language (name_language,last_update) VALUES ('German','2006-02-15' );

INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17503,1,2,101,7.99,'2007-02-15');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17504,1,1,102,1.99,'2007-02-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17505,1,1,103,7.99,'2007-02-16'):
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17506,1,2,104,2.99,'2007-12-19');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17507,1,2,105,7.99,'2007-12-20');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17508,1,1,106,5.99,'2007-11-21');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17509,2,2,107,5.99,'2007-10-17');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17510,2,1,108,5.99,'2007-10-20');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17511,2,1,109,2.99,'2007-09-20');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17512,3,2,110,4.99,'2007-08-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17513,3,1,111,6.99,'2007-08-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17514,3,2,112,0.99,'2007-08-17');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17515,3,2,113,0.99,'2007-07-17');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17516,3,2,114,6.99,'2007-07-18');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17517,3,1,115,8.99,'2007-07-20');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17518,3,1,116,0.99,'2007-07-21');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17519,4,1,117,3.99,'2007-06-15');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17520,4,2,118,4.99,'2007-02-15');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17521,4,1,119,0.99,'2007-06-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17522,5,2,120,0.99,'2007-06-15');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17523,5,1,121,4.99,'2007-05-15');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17524,5,2,122,0.99,'2007-02-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17525,5,2,123,4.99,'2007-03-19');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17545,1,2,124,5.99,'2007-03-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17546,1,1,125,0.99,'2007-05-17');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17547,1,1,126,2.99,'2007-05-19');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17548,2,1,127,0.99,'2007-05-15');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17549,2,1,128,4.99,'2007-05-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17550,2,1,129,4.99,'2007-05-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17551,2,1,130,4.99,'2007-03-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (17552,2,2,131,4.99,'2007-03-21');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18516,3,2,114,6.99,'2007-07-18');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18517,3,1,115,8.99,'2007-07-20');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18518,3,1,116,0.99,'2007-07-21');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18519,4,1,117,3.99,'2007-06-15');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18520,4,2,118,4.99,'2007-02-15');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18521,4,1,119,0.99,'2007-06-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18522,5,2,120,0.99,'2007-06-15');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18523,5,1,121,4.99,'2007-11-15');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18524,5,2,122,0.99,'2007-11-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18525,5,2,123,4.99,'2007-12-19');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18545,1,2,124,5.99,'2007-12-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18546,1,1,125,0.99,'2007-12-17');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18547,1,1,126,2.99,'2007-10-19');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18548,2,1,127,0.99,'2007-10-15');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18549,2,1,128,4.99,'2007-09-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18550,2,1,129,4.99,'2007-09-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18551,2,1,130,4.99,'2007-09-16');
INSERT INTO payment (payment_id,customer_id,staff_id,rental_id,amount,payment_date) VALUES (18552,2,2,131,4.99,'2007-09-21');


INSERT INTO staff (first_name,last_name,address_id,email,store_id,active,username,password,last_update) VALUES ('Mike','Hillyer',1,'Mike.Hillyer@sakilastaff.com',1,'True','Mike','1234','2006-05-16');
INSERT INTO staff (first_name,last_name,address_id,email,store_id,active,username,password,last_update) VALUES ('Jon','Stephens',2,'MJon.Stephens@sakilastaff.com',2,'True','Jon','5678','2006-05-16');

INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (101,'2005-05-25',1,1,'2005-06-02',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (102,'2005-05-24',2,1,'2005-05-28',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (103,'2005-06-24',3,1,'2005-06-01',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (104,'2005-06-24',4,1,'2005-06-03',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (105,'2005-06-24',5,1,'2005-06-02',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (106,'2005-06-24',6,1,'2005-05-27',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (107,'2005-06-24',7,1,'2005-05-29',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (108,'2005-06-24',8,2,'2005-05-27',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (109,'2005-06-25',9,3,'2005-05-28',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (110,'2005-06-25',10,2,'2005-05-31',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (111,'2005-06-25',1,2,'2005-06-02',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (112,'2005-06-25',2,2,'2005-05-30',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (113,'2005-05-25',3,2,'2005-05-30',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (114,'2005-05-25',1,3,'2005-05-26',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (115,'2005-05-25',1,3,'2005-06-03',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (116,'2005-05-25',2,3,'2005-05-26',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (117,'2005-05-25',2,3,'2005-05-27',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (118,'2005-05-25',3,4,'2005-05-31',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (119,'2005-05-25',4,5,'2005-05-31',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (120,'2006-05-25',5,5,'2005-05-27',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (121,'2006-05-25',5,5,'2005-05-26',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (122,'2006-05-25',5,5,'2005-05-26',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (123,'2006-05-25',5,3,'2005-05-29',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (124,'2006-05-25',6,3,'2005-05-27',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (125,'2006-05-25',7,3,'2005-05-27',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (126,'2006-05-25',7,3,'2005-05-31',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (127,'2006-05-25',7,3,'2005-05-30',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (128,'2006-05-25',8,3,'2005-05-26',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (129,'2006-05-25',3,2,'2005-05-30',2,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (130,'2006-05-25',3,2,'2005-05-30',1,'2006-02-16');
INSERT INTO rental (rental_id,rental_date,inventory_id,customer_id,return_date,staff_id,last_update) VALUES (131,'2006-05-25',3,2,'2005-05-30',1,'2006-02-16');
