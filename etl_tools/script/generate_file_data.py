from ..mongodb_simulator.tools.mongodb_generator_data import DriverGenerator, VehicleGenerator

DriverGenerator(10, generate_file=True).generate()
VehicleGenerator(10, generate_file=True).generate()