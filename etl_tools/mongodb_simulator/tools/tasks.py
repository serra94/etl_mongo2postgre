from celery import Celery

from mongodb_simulator import simulate_data
from mongodb_generator_data import DriverGenerator, VehicleGenerator, ClientGenerator

app = Celery(
    broker='amqp://admin:admin@localhost:5672//'
)

db_address = 'mongodb://localhost:27017/'
db_name = 'montogre'

@app.task
def simulate_driver_data():
    simulate_data(db_address, db_name, DriverGenerator)

@app.task
def simulate_vehicle_data():
    simulate_data(db_address, db_name, VehicleGenerator)

@app.task
def simulate_client_data():
    simulate_data(
        db_address, db_name, 
        ClientGenerator, 
        custom_actions=['create']
    )