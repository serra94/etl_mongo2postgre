from faker import Faker
import random
import json



def data_creator(times):

    with open('extracted_data.json', 'r') as extracted_data:
        data = json.load(extracted_data)
    
    longitude_latitude = data["extracted_data"]
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
        deliver_drive["origin_gps"] = random.choice(longitude_latitude)
        deliver_drive["destination"] = fake.street_address()
        deliver_drive["destination_gps"] = random.choice(longitude_latitude)
        deliver_drive["estimated_time"] = str(random_hours) + ":" + str(random_minutes)
       
        

        collections.append(deliver_drive)

    output_file = "collection.json"

    with open(output_file, "w") as outfile:
        json.dump(collections, outfile, indent=4)

    return f"Extracted data has been saved to {output_file}"
    




test_1 = data_creator(10)

print(test_1)
