import random

from src import *  # This import should be replaced with `import rcplant`


def user_sorting_function(sensors_output):
    # random identification
    print(sensors_output)
    input()
    decision = {sensor_id: random.choice(list(Plastic)) for (sensor_id, value) in sensors_output.items()}

    return decision


def main():

    # simulation parameters
    conveyor_length = 1000  # cm
    conveyor_width = 100  # cm
    conveyor_speed = 10  # cm per second
    num_containers = 100
    sensing_zone_location_1 = 500  # cm
    sensing_zone_location_2 = 600  # cm
    sensors_sampling_frequency = 1  # Hz
    simulation_mode = 'training'

    sensors = [
        Sensor.create(SpectrumType.FTIR, sensing_zone_location_1),
        Sensor.create(SpectrumType.Raman, sensing_zone_location_2),
    ]

    conveyor = Conveyor.create(conveyor_speed, conveyor_length, conveyor_width)

    simulator = RPSimulation(
        sorting_function=user_sorting_function,
        num_containers=num_containers,
        sensors=sensors,
        sampling_frequency=sensors_sampling_frequency,
        conveyor=conveyor,
        mode=simulation_mode
    )

    elapsed_time = simulator.run()

    print(f'\nResults for running the simulation in "{simulation_mode}" mode:')
    print(f'Total missed containers = {simulator.total_missed}')
    print(f'Total sorted containers = {simulator.total_classified}')
    print(f'Total mistyped containers = {simulator.total_mistyped}')

    print(f'\n{num_containers} containers are processed in {elapsed_time:.2f} seconds')


if __name__ == '__main__':
    main()
