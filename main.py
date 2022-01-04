import random

from src import *  # This import should be replaced with `import rcplant`


def user_sorting_function(sensors_output):
    # random identification
    decision = {guid: random.choice(list(Plastic)) for (guid, value) in sensors_output.items()}

    return decision


def main():

    # simulation parameters
    conveyor_length = 1000  # cm
    conveyor_speed = 10  # cm per second
    num_containers = 100
    sensing_zone_location_1 = 500  # cm
    sensing_zone_location_2 = 600  # cm
    sensors_sampling_frequency = 2  # Hz
    simulation_mode = 'testing'

    sensors = [
        Sensor(sensing_zone_location_1, SpectrumType.FTIR),
        Sensor(sensing_zone_location_2, SpectrumType.Raman),
    ]

    for index, sensor in enumerate(sensors):
        print(f'The unique ID for sensor[{index}]: {sensor.guid}')

    conveyor = Conveyor(conveyor_speed, conveyor_length)

    simulator = RPSimulation(
        sorting_function=user_sorting_function,
        num_containers=num_containers,
        sensors=sensors,
        sampling_frequency=sensors_sampling_frequency,
        conveyor=conveyor,
        mode=simulation_mode
    )

    elapsed_time = simulator.run()

    print(f'\nTotal missed containers = {simulator.total_missed}')
    print(f'Total sorted containers = {simulator.total_classified}')
    print(f'Total mistyped containers = {simulator.total_mistyped}')

    print(f'\n{num_containers} containers are processed in {elapsed_time:.2f} seconds')


if __name__ == '__main__':
    main()
