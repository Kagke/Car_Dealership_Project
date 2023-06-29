import pdb

from models.manufacturer import Manufacturer
from models.car import Car


import repositories.manufacturer_repository as manufacturer_repository
import repositories.car_repository as car_repository

car_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer_1 = Manufacturer("Mercedes-Benz Group", "345-654-604", "mercedes.group@info.com")
manufacturer_repository.save(manufacturer_1)
manufacturer_2 = Manufacturer("Audi AG", "457-591-044", "audi.ag@info.com")
manufacturer_repository.save(manufacturer_2)
manufacturer_3 = Manufacturer("Ferrari S.p.A.", "623-555-091", "ferrari.spa.@info.com")
manufacturer_repository.save(manufacturer_3)
manufacturer_4 = Manufacturer("Automobili Lamborghini S.p.A.", "846-098-231", "lamborghini.auto.modile@info.com")
manufacturer_repository.save(manufacturer_4)
manufacturer_5 = Manufacturer("Bugatti Automobiles S.A.S.", "536-531-165", "mercedes.group@info.com")
manufacturer_repository.save(manufacturer_5)

manufacturer_1.email = "mercedes-benz.group@info.com"
manufacturer_repository.update(manufacturer_1)
#manufacturer_repository.delete(manufacturer_1.id)

# manufacturer_id_8 = manufacturer_repository.select_by_id(8)

manufacturers = manufacturer_repository.select_all()


car_1 = Car("Mercendes-Benz", "AMG 306", 3, 60000, 67000, manufacturer_1)
car_repository.save(car_1)
car_2 = Car("Audi", "R9", 1, 70000, 82000, manufacturer_2 )
car_repository.save(car_2)
car_3 = Car("Ferrari", "California", 1, 67000, 80000, manufacturer_3)
car_repository.save(car_3)
car_4 = Car("Lamborghini", "Aventador", 2, 82000, 110000, manufacturer_4)
car_repository.save(car_4)
car_5 = Car("Buggati", "Chiron", 1, 1000000, 1700000, manufacturer_5)
car_repository.save(car_5)


car_2.model = "R8"
car_repository.update(car_2)

#car_id_18 = car_repository.select_by_id(18)
#car_repository.delete(car_1.id)
cars = car_repository.select_all()
pdb.set_trace()