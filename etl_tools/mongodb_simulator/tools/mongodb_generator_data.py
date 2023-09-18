import json
import os
import random
from faker import Faker

class DataGenerator:
    def __init__(self):
        self.fake = Faker('pt_BR')

    def generate_data(self):
        raise NotImplementedError("Subclasses devem implementar este método")

    def generate(self, quantity=1, generate_file=False, output_path='../data'):
        self.quantity = quantity
        self.generate_file = generate_file
        self.output_path = output_path

        data = self.generate_data()
        collection_name = data[0]
        
        if self.generate_file:
            documents = data[1]
            file_path = os.path.join(self.output_path, f'{collection_name}.json')
            with open(file_path, 'w') as json_file:
                json.dump(documents, json_file, indent=2)
        else:
            document = data[1]
            return collection_name, document

class DriverGenerator(DataGenerator):
    def generate_data(self):
        collection_name = 'DriverCollection'
        drivers = [{
            'name': self.fake.name(),
            'cnh_number': self.fake.ssn(),
            'address': self.fake.address(),
            'phone_number': self.fake.phone_number(),
            'e-mail': self.fake.ascii_free_email()
        } for _ in range(self.quantity)]
        return collection_name, drivers

class VehicleGenerator(DataGenerator):
    def generate_data(self):
        collection_name = 'VehicleCollection'
        vehicles = [{
            'name': random.choice(['Truck', 'Báu', 'Van', 'Mini-Cargo']),
            'vehicle_plate': self.fake.license_plate(),
            'dimensions': {
                "length": round(random.uniform(0.0, 5.0), 1),
                "width": round(random.uniform(0.0, 5.0), 1),
                "height": round(random.uniform(0.0, 5.0), 1)
            }
        } for _ in range(self.quantity)]
        return collection_name, vehicles

class ClientGenerator(DataGenerator):
    def generate_data(self):
        collection_name = 'ClientCollection'
        clients = [{
            'name': f'{self.fake.company()} {self.fake.company_suffix()}',
            'cnpj': self.fake.cnpj()

        } for _ in range(self.quantity)]
        return collection_name, clients