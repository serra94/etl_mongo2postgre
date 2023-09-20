import csv
from faker import Faker
import json
import os
import random

class DataGenerator:
    def __init__(self):
        self.fake = Faker('pt_BR')

    def generate_data(self):
        raise NotImplementedError(
            "Subclasses devem implementar este método"
        )

    def generate(self, quantity=1, generate_file=False, output_path='../data/data_generated'):
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
                'length': round(random.uniform(0.0, 5.0), 1),
                'width': round(random.uniform(0.0, 5.0), 1),
                'height': round(random.uniform(0.0, 5.0), 1)
            }
        } for _ in range(self.quantity)]
        return collection_name, vehicles

class ClientGenerator(DataGenerator):
    def generate_data(self):
        collection_name = 'ClientCollection'
        clients = [{
            'name': f'{self.fake.company()} {self.fake.company_suffix()}',
            'cnpj': self.fake.cnpj(),
            #NEW - OPEN
            'address': self.fake.address(),
            'phone_number': self.fake.phone_number(),
            'e-mail': self.fake.ascii_free_email()
            #NEW - CLOSE
            # CONTINUAR A COMPLETAR O DOC

        } for _ in range(self.quantity)]
        return collection_name, clients
    
class LocationGenerator(DataGenerator):
    def generate_data(self):
        collection_name = 'LocationCollection'
        location = [self.get_location_data() for _ in range(self.quantity)]
        return collection_name, location

    @classmethod
    def get_location_data(cls):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, '..', 'data/data_to_build', 'municipios.csv')
        
        locations = {}
        
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            read = csv.reader(csvfile, delimiter=',')
    
            next(read)
    
            data = list(read)
            
            row = random.choice(data)
            city_id = row[0]
            city_name = row[1]
            latitude = row[2]
            longitude = row[3]
            locations = {
                'city_id': city_id,
                'city_name': city_name,
                'coordinates': {
                    'latitude': latitude,
                    'longitude': longitude
                }   
            }
        
        return locations

class ProductGenerator(DataGenerator):
    def generate_data(self):
        collection_name = 'ProductCollection'
        location = [self.get_product_data() for _ in range(self.quantity)]
        return collection_name, location

    @classmethod
    def get_product_data(cls):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, '..', 'data/data_to_build', 'products.json')
        
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            
            product = random.choice(data)
            
            return product
        
class DeliveryGenerator(DataGenerator):
    def generate_data(self):
        collection_name = 'DeliveryCollection'

        build_driver = DriverGenerator()
        build_vehicle = VehicleGenerator()
        build_client = ClientGenerator()
        build_location = LocationGenerator()
        build_product = ProductGenerator()
        # CONTINUAR A COMPLETAR O DOC

        deliverys = [{

            'driver': build_driver.generate()[1][0],
            'vehicle': build_vehicle.generate()[1][0],
            'client': build_client.generate()[1][0],
            'data_delivery': {
                'data_start': "",
                'origin': build_location.generate()[1][0],
                'destination': build_location.generate()[1][0],
                'product': build_product.generate()[1][0]
                }
            
            # CONTINUAR A COMPLETAR O DOC COM AS DEMAIS CLASSES.

            # COM "LocationGenerate" TALVEZ SERÁ NECESSÁRIO INTRODUZIR UMA
            # LÓGICA PARA NÃO REPETIR ENDEREÇOS.

            # COMPREMENTAR COM DATAS DE DOIS TIPOS (timestamp e Z)

        } for _ in range(self.quantity)]
        return collection_name, deliverys