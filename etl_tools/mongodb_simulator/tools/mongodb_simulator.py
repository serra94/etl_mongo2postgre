import time
import random
from mongodb_actions import MongoDBActions

def simulate_data(db_address, db_name, data_generator_class, time_action=5, custom_actions=None):
    while True:
        if custom_actions:
            action = random.choice(custom_actions)
        else:
            action = random.choice(['create', 'update', 'delete'])

        if action == 'create' or action == 'update':
            data_document_instance = data_generator_class()
            data_document = data_document_instance.generate()
            simulator = MongoDBActions(
                db_address, 
                db_name, 
                data_document[0], 
                data_document[1][0]
            )
            if action == 'create':
                simulator.create_document()
                print('ADD DOCUMENT')
            else:
                simulator.update_document()
                print('UPDATE DOCUMENT')
        else:
            data_document_instance = data_generator_class()
            data_document = data_document_instance.generate()
            simulator = MongoDBActions(
                db_address, 
                db_name, 
                data_document[0], 
                data_document[1][0]
            )
            simulator.delete_document()
            print('DELETE DOCUMENT')

        time.sleep(random.uniform(1, time_action))
