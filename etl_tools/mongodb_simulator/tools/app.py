from mongodb_generator_data import DriverGenerator, VehicleGenerator, ClientGenerator
from mongodb_simulator import DataSimulator
import threading

db_address = 'mongodb://localhost:27017/'
db_name = 'montogre'

if __name__ == "__main__":
    
    simulator_driver = DataSimulator(db_address, db_name, 1, DriverGenerator)
    simulator_driver_thread = threading.Thread(target=simulator_driver.simulate_data)

    simulator_vehicle = DataSimulator(db_address, db_name, 1, VehicleGenerator)
    simulator_vehicle_thread = threading.Thread(target=lambda: simulator_vehicle.simulate_data(['create']))

    simulator_client = DataSimulator(db_address, db_name, 1, ClientGenerator)
    simulator_client_thread = threading.Thread(target=lambda: simulator_client.simulate_data(['create']))

    simulator_driver_thread.start()
    simulator_vehicle_thread.start()
    simulator_client_thread.start()

    simulator_driver_thread.join()
    simulator_vehicle_thread.join()
    simulator_client_thread.join()
