from _simulation import RPSimulation
from _material import Plastic
import random


def user_sorting_function(sensor_output):
    if sensor_output is not None:
        print(sensor_output)
        # exact identification
        # return Plastic(sensor_output.index.values[0])

        # random identificatio
        return random.choice(list(Plastic))


def main():
    final_time = 10 * 60 * 60
    delta_t = 1
    simulator = RPSimulation(user_sorting_function, final_time, delta_t)

    simulator.run()

    print(f'Total missed container = {simulator.total_missed}')
    print(f'Total sorted container = {simulator.total_classified}')
    print(f'Total mistyped container = {simulator.total_mistyped}')


if __name__ == '__main__':
    main()
