import json
import os
import random
from faker import Faker

class DriverGenerator:
    def __init__(self, quantity= 1, name='DriversCollection', generate_file=False, output_path='../data'):
        self.fake = Faker('pt_BR')
        self.quantity = quantity
        self.name = name
        self.generate_file = generate_file
        self.output_path = output_path

    def generate_driver(self):
        driver = {
            'name': self.fake.name(),
            'cnh_number': self.fake.ssn(),
            'address': self.fake.address(),
            'phone_number': self.fake.phone_number(),
            'e-mail': self.fake.ascii_free_email()
        }
        return driver

    def generate_drivers(self):
        drivers = [self.generate_driver() for _ in range(self.quantity)]
        return drivers

    def generate(self):
        if self.generate_file:
            drivers = self.generate_drivers()
            file_path = os.path.join(self.output_path, f'{self.name}.json')
            with open(file_path, 'w') as json_file:
                json.dump(drivers, json_file, indent=2)
        else:
            drivers = [self.generate_driver()]
            return self.name, drivers

class VehicleGenerator:
    def __init__(self, quantity= 1, name='VehicleCollection', generate_file=False, output_path='../data'):
        self.fake = Faker('pt_BR')
        self.quantity = quantity
        self.name = name
        self.generate_file = generate_file
        self.output_path = output_path

    def generate_vehicle(self):
        vehicle = {
            'name': random.choice(['Truck', 'Báu', 'Van', 'Mini-Cargo']),
            'vehicle_plate': self.fake.license_plate(),
            'dimensions': {
                "length": round((random.uniform(0.0, 5.0)), 1), 
                "width": round((random.uniform(0.0, 5.0)), 1),
                "height": round((random.uniform(0.0, 5.0)), 1) 
            }
        }

        return vehicle

    def generate_vehicles(self):
        vehicles = [self.generate_vehicle() for _ in range(self.quantity)]
        return vehicles

    def generate(self):
        if self.generate_file:
            vehicles = self.generate_vehicles()
            file_path = os.path.join(self.output_path, f'{self.name}.json')
            with open(file_path, 'w') as json_file:
                json.dump(vehicles, json_file, indent=2)
        else:
            vehicles = [self.generate_vehicle()]
            return self.name, vehicles