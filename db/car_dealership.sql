DROP TABLE IF EXISTS cars;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone_number VARCHAR(255)
);

CREATE TABLE cars(
    id SERIAL PRIMARY KEY ,
    make VARCHAR(255),
    model VARCHAR(255),
    stock_quantity INT ,
    buying_cost INT , 
    selling_price INT,
    manufacturer_id INT REFERENCES manufacturers(id)
);
