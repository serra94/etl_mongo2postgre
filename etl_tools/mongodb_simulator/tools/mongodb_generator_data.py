import json
import os
import random
from faker import Faker

class DataGenerator:
    def __init__(self, quantity=1, name='Collection', generate_file=False, output_path='../data'):
        self.fake = Faker('pt_BR')
        self.quantity = quantity
        self.name = name
        self.generate_file = generate_file
        self.output_path = output_path

    def generate_data(self):
        raise NotImplementedError("Subclasses devem implementar este método")

    def generate(self):
        data = self.generate_data()
        if self.generate_file:
            file_path = os.path.join(self.output_path, f'{self.name}.json')
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=2)
        else:
            return self.name, data

class DriverGenerator(DataGenerator):
    def generate_data(self):
        drivers = [{
            'name': self.fake.name(),
            'cnh_number': self.fake.ssn(),
            'address': self.fake.address(),
            'phone_number': self.fake.phone_number(),
            'e-mail': self.fake.ascii_free_email()
        } for _ in range(self.quantity)]
        return drivers

class VehicleGenerator(DataGenerator):
    def generate_data(self):
        vehicles = [{
            'name': random.choice(['Truck', 'Báu', 'Van', 'Mini-Cargo']),
            'vehicle_plate': self.fake.license_plate(),
            'dimensions': {
                "length": round(random.uniform(0.0, 5.0), 1),
                "width": round(random.uniform(0.0, 5.0), 1),
                "height": round(random.uniform(0.0, 5.0), 1)
            }
        } for _ in range(self.quantity)]
        return vehicles

class ClientGenerator(DataGenerator):
    def generate_data(self):
        clients = [{
            'name': f'{self.fake.company()} {self.fake.company_suffix()}',
            'cnpj': self.fake.cnpj()

        } for _ in range(self.quantity)]
        return clients