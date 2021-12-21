import random

from src import *  # This import should be replaced with `import rcplant`


def user_sorting_function(sensors_output):
    # ignore sensors and do nothing
    # decision = {}

    # random identification
    # print(sensors_output)
    decision = {guid: random.choice(list(Plastic)) for (guid, value) in sensors_output.items()}
    # for key, value in sensors_output.items():
    #     if value['spectrum'] != 0:
    #         print(value['spectrum'])
    #         return 0
    # print(sensors_output)
    return decision


def main():
    final_time_min = 60 * 10
    conveyor_speed = 1  # cm per second
    conveyor_length = 1000  # cm
    sensing_zone_location_1 = 500  # cm
    sensing_zone_location_2 = 600  # cm
    simulation_mode = 'training'

    sensors = [
        Sensor(sensing_zone_location_1, SpectrumType.FTIR),
        Sensor(sensing_zone_location_2, SpectrumType.Raman),
    ]

    conveyor = Conveyor(conveyor_speed, conveyor_length)

    simulator = RPSimulation(
        sorting_function=user_sorting_function,
        final_time_min=final_time_min,
        sensors=sensors,
        conveyor=conveyor,
        mode=simulation_mode
    )

    simulator.run()

    print(f'Total missed container = {simulator.total_missed}')
    print(f'Total sorted container = {simulator.total_classified}')
    print(f'Total mistyped container = {simulator.total_mistyped}')


if __name__ == '__main__':
    main()
