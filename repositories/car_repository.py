from db.run_sql import run_sql
from models.car import Car
import repositories.manufacturer_repository as manufacturer_repository

def save(car):
    sql = "INSERT INTO cars (make, model, stock_quantity, buying_cost, selling_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [car.make, car.model, car.stock_quantity, car.buying_cost, car.selling_price, car.manufacturer.id]
    results = run_sql(sql, values)
    car.id = results[0]['id']
    return car


def select_all():
    cars = []
    sql = "SELECT * FROM cars"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select_by_id(row['manufacturer_id'])
        car = Car(row['make'], row['model'], row['stock_quantity'], row['buying_cost'], row['selling_price'], manufacturer, row['id'])
        cars.append(car)
    return cars

def select_by_id(id):
    car = None
    sql = "SELECT * FROM cars WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select_by_id(result['manufacturer_id'])
        car = Car(result['make'], result['model'], result['stock_quantity'], result['buying_cost'], result['selling_price'], manufacturer, result['id'])
    return car

def delete_all():
    sql = "DELETE FROM cars"
    
    run_sql(sql)



def delete(id):
    sql = "DELETE FROM cars WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def cars_for_manufacturer(manufacturer):
    cars = []

    sql = "SELECT * FROM cars WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        manufacturer = manufacturer_repository.select_by_id(row['manufacturer_id'])
        car = Car(row['make'], row['model'], row['stock_quantity'], row['buying_cost'], row['selling_price'], manufacturer, row['id'] )
        cars.append(car)
    return cars

def update(car):
    sql = "UPDATE cars SET (make, model, stock_quantity, buying_cost, selling_price, manufacturer_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [car.make, car.model, car.stock_quantity ,car.buying_cost, car.selling_price, car.manufacturer.id, car.id]
    run_sql(sql, values)