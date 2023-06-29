from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.car import Car
import repositories.car_repository as car_repository
import repositories.manufacturer_repository as manufacturer_repository

car_blueprint = Blueprint("cars", __name__)


@car_blueprint.route("/cars")
def cars():

    cars = car_repository.select_all() # NEW
    return render_template("/cars/index.html", cars = cars)

# NEW

@car_blueprint.route("/cars/new", methods=['GET'])
def new_car():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/cars/new.html", manufacturers = manufacturers)

# CREATE

@car_blueprint.route("/cars",  methods=['POST'])
def create():

    make = request.form['make']
    model = request.form['model']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    manufacturer_id = request.form['manufacturer_id']
    manufacturer = manufacturer_repository.select_by_id(manufacturer_id)
    car = Car(make, model, stock_quantity, buying_cost, selling_price, manufacturer)
    car_repository.save(car)
    return redirect('/cars')

#SHOW
@car_blueprint.route('/cars/<id>')
def show(id):
    car = car_repository.select_by_id(id)
    manufacturer = manufacturer_repository.select_by_id(id)
    return render_template("/cars/show.html", car = car , manufacturer = manufacturer)

#edit
@car_blueprint.route("/cars/<id>/edit")
def edit(id):
    car = car_repository.select_by_id(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template("/cars/edit.html", car = car, manufacturers = manufacturers)

#Update
@car_blueprint.route("/cars/<id>" , methods = ["POST"])
def update(id):
    make = request.form['make']
    model = request.form['model']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    manufacturer_id = request.form['manufacturer_id']
    manufacturer = manufacturer_repository.select_by_id(manufacturer_id)
    car = Car(make, model, stock_quantity, buying_cost, selling_price, manufacturer, id)

    car_repository.update(car)
    return redirect ('/cars')

# DELETE
# DELETE '/visits/<id>'
@car_blueprint.route("/cars/<id>/delete", methods=['POST'])
def delete(id):
    car = car_repository.delete(id)
    return redirect('/cars')

