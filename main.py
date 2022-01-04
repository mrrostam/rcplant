import random

from src import *  # This import should be replaced with `import rcplant`


def user_sorting_function(sensors_output):
    # ignore sensors and do nothing
    # decision = {}

    # random identification
    decision = {guid: random.choice(list(Plastic)) for (guid, value) in sensors_output.items()}
    # for key, value in sensors_output.items():
    #     if value['spectrum'] != 0:
    #         print(value['spectrum'])
    #         return 0
    # print(sensors_output)

    return decision


def main():
    conveyor_length = 1000  # cm
    conveyor_speed = 10  # cm per second
    num_containers = 1000
    sensing_zone_location_1 = 500  # cm
    sensing_zone_location_2 = 600  # cm
    sensors_sampling_frequency = 2  # Hz
    simulation_mode = 'training'

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

    simulator.run()

    print(f'\nTotal missed containers = {simulator.total_missed}')
    print(f'Total sorted containers = {simulator.total_classified}')
    print(f'Total mistyped containers = {simulator.total_mistyped}')


if __name__ == '__main__':
    main()
