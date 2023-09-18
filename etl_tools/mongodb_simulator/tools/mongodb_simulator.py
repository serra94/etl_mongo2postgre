import time
import random
import threading
from mongodb_actions import MongoDBActions

class DataSimulator:
    def __init__(self, db_address, db_name, num_threads, data_generator_class, time_action=5):
        self.db_address = db_address
        self.db_name = db_name
        self.num_threads = num_threads
        self.data_generator_class = data_generator_class
        self.time_action = time_action

    def simulate_data(self, custom_actions=None):
        def simulator_driver_data():
            while True:
                if custom_actions:
                    action = random.choice(custom_actions)
                else:
                    action = random.choice(['create', 'update', 'delete'])
                
                if action == 'create' or action == 'update':
                    data_document = self.data_generator_class().generate()
                    simulator = MongoDBActions(
                        self.db_address, 
                        self.db_name, 
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
                    data_document = self.data_generator_class().generate()
                    simulator = MongoDBActions(
                        self.db_address, 
                        self.db_name, 
                        data_document[0], 
                        data_document[1][0]
                    )
                    simulator.delete_document()
                    print('DELETE DOCUMENT')
                
                time.sleep(random.uniform(1, self.time_action))

        threads = []

        for _ in range(self.num_threads):
            thread = threading.Thread(target=simulator_driver_data)
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()