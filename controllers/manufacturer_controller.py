from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.manufacturer_repository as manufacturer_repository
import repositories.car_repository as car_repository
from models.manufacturer import Manufacturer

manufacturer_blueprint = Blueprint("manufacturers", __name__)

#INDEX
@manufacturer_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all() 
    return render_template("manufacturers/index.html", manufacturers = manufacturers)

#SHOW 1

#NEW 
#route to new.html to add a manufacturer
@manufacturer_blueprint.route("/manufacturers/new", methods=['GET'])
def new_manufacturer():
    return render_template("manufacturers/new.html") 

#CREATE
@manufacturer_blueprint.route("/manufacturers",  methods=['POST'])
def create():
    name = request.form['name']
    phone_number = request.form['phone_number']
    email= request.form['email']
    
    manufacturer = Manufacturer(name , phone_number , email)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')
#EDIT
@manufacturer_blueprint.route("/manufacturers/<id>/edit")
def edit(id):
    
    manufacturer = manufacturer_repository.select_by_id(id)
    return render_template("/manufacturers/edit.html" , manufacturer = manufacturer)
#UPDATE

@manufacturer_blueprint.route("/manufacturers/<id>" , methods = ["POST"])
def update(id):
    name = request.form['name']
    phone_number = request.form['phone_number']
    email = request.form['email']
    manufacturer = Manufacturer(name, phone_number, email ,id)
    
    manufacturer_repository.update(manufacturer)
    
    return redirect ('/manufacturers')

