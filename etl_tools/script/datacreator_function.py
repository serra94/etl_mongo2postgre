from faker import Faker
import random
import json
import csv
import os


def get_location_data(file_name):
    '''
    Provide the name of the file you want to use. By default the file must be 
    in the "data" folder within the "etl_tools" directory

    Ex: get_location_data('FILE_NAME.csv')
    '''

    '''
    Nesse trecho retorna o caminho do arquivo que está sendo executado
    '''
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f'\n{script_dir}')

    '''
    Nesse trecho concatenamos os caminho, usamo '..' para voltar um diretório
    '''

    file_path = os.path.join(script_dir, '..', 'data', file_name)
    print(f'\n{file_path}')
    
    locations = {}
    
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        read = csv.reader(csvfile, delimiter=',')

        ''' 
        Utilizamos 'next()' para pular a primeira linha do .csv que
        geralemte se trata de um cabeçalho.
        '''
        next(read)

        data = list(read)
        
        for i in range(1):
            row = random.choice(data)
            city_id = row[0]
            latitude = row[2]
            longitude = row[3]
            locations[f'location_{i + 1}'] = {
                'id': city_id,
                'latitude': latitude,
                'longitude': longitude
            }
    
    return locations

'''
Você pode usar os comandos abaixo para entender as saídas que essa função
produz:

    locations = get_location_data('municipios.csv')
    print(locations)
'''

'''
Acredito que a sua função 'data_creator' pode receber um parâmetro NÃO 
obrigatório/opcional para você indicar um arquivo para dar as localizações.
Dessa forma temos espaço pra se caso a base de dados for ampliada ou alterada.
'''

def data_creator(times):

    fake = Faker('pt_BR')
    vehicle_type_list = ["Truck", "Van", "Baú", "Mini Cargo"]
    random_hours = random.randint(1, 23)
    random_minutes = random.randint(0, 59)
    collections = []

    for time in range(times):

        deliver_drive = {}

        deliver_drive["name"] = fake.name()
        deliver_drive["cpf"] = fake.cpf()
        deliver_drive["driver_license"] = ""
        deliver_drive["phone"] = fake.cellphone_number() 
        deliver_drive["vehicle_plate"] = fake.license_plate()
        deliver_drive["vehicle_dimensions"] = {"length":round((random.uniform(0.0, 5.0)), 1), "width":round((random.uniform(0.0, 5.0)), 1),"height":round((random.uniform(0.0, 5.0)), 1)}
        deliver_drive["vehicle_type"] = random.choice(vehicle_type_list)
        deliver_drive["origin"] = fake.street_address()
        deliver_drive["origin_gps"] = get_location_data('municipios.csv')
        deliver_drive["destination"] = fake.street_address()
        deliver_drive["destination_gps"] = get_location_data('municipios.csv')
        deliver_drive["estimated_time"] = str(random_hours) + ":" + str(random_minutes)
       
        collections.append(deliver_drive)

    folder_path = "etl_tools/data"
    file_name = "collection.json"
    output_file = os.path.join(folder_path, file_name)

    with open(output_file, "w") as outfile:
        json.dump(collections, outfile, indent=4)

    return f"Extracted data has been saved to {output_file}"
    
test_1 = data_creator(5)

print(test_1)
