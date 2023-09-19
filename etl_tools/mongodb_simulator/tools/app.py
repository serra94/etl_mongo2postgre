from tasks import simulate_driver_data, simulate_vehicle_data, simulate_client_data

simulate_driver_data.delay()
simulate_vehicle_data.delay()
simulate_client_data.delay()
