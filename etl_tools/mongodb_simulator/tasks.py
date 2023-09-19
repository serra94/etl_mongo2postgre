from celery import Celery

from mongodb_simulator import simulate_data
from mongodb_generator_data import DeliveryGenerator, ClientGenerator

app = Celery(
    broker='amqp://admin:admin@localhost:5672//'
)

db_address = 'mongodb://localhost:27017/'
db_name = 'montogre'

@app.task
def simulate_delivery_data():
    simulate_data(db_address, db_name, DeliveryGenerator, custom_actions=['create'])

@app.task
def simulate_client_data():
    simulate_data(db_address, db_name, ClientGenerator, editing_grade=50)
