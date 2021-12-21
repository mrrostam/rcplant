import random
import types
from typing import List

from ._container import *
from ._conveyor import *
from ._enums import SimulationMode
from ._sensor import *

DEFAULT_CONVEYOR_POSITION = 1000
DEFAULT_CONVEYOR_SPEED = 1
DEFAULT_SENSOR_POSITION = 500

MIN_CONTAINER_WIDTH = 5
MAX_CONTAINER_WIDTH = 15


class RecyclingPlant:
    def __init__(self, sorting_function, conveyor: Conveyor = None, sensors: List[Sensor] = None, mode=None):
        if not isinstance(sorting_function, types.FunctionType):
            raise ValueError(f'Invalid sorting function, please passl a compatible function')

        if not any(mode == simulation_mode.value for simulation_mode in SimulationMode):
            raise ValueError(f'Invalid simulation mode , \n'
                             f'valid options: {[mode.value for mode in SimulationMode]}')

        self._user_sorting_function = sorting_function
        self._mode = mode

        if conveyor is None:
            self._conveyor = Conveyor(DEFAULT_CONVEYOR_SPEED, DEFAULT_CONVEYOR_POSITION)
        else:
            self._conveyor = conveyor

        if sensors is None:
            self._sensors = [
                Sensor(DEFAULT_SENSOR_POSITION, SpectrumType.FTIR),
            ]
        else:
            self._sensors = sensors

        self._containers_list = []

    @staticmethod
    def _is_visible_to_sensor(sensor: Sensor, container: Container):
        return container.location > sensor.location > (container.location - container.dimension)

    def _add_container(self, plastic_type: Plastic, dimension: int):
        self._containers_list.append(Container(plastic_type, dimension))

    def update(self, time_step_sec: float, generate_container: bool):
        missed = 0
        classified = 0
        mistyped = 0
        sensors_output = {}
        sensed_containers = {}

        for sensor in self._sensors:  # init sensor_output with the background spectrum
            sensors_output.update(
                {
                    sensor.guid: {
                        'type': sensor.type,
                        'location_cm': sensor.location,
                        'spectrum': sensor.read(None, self._mode),
                    }
                }
            )

        for container in self._containers_list:
            container.location += time_step_sec * self._conveyor.speed
            if container.location >= self._conveyor.length:
                self._containers_list.remove(container)
                missed += 1  # container reached the end of the conveyor
            for sensor in self._sensors:
                if self._is_visible_to_sensor(sensor, container):
                    sensors_output.update(
                        {
                            sensor.guid: {
                                'type': sensor.type,
                                'location_cm': sensor.location,
                                'spectrum': sensor.read(container, self._mode),
                            }
                        }
                    )
                    sensed_containers.update(
                        {
                            sensor.guid: container
                        }
                    )

        # generating new containers
        if random.random() > 0.5 and generate_container:
            if not self._containers_list or (
                    self._containers_list[-1].location - self._containers_list[-1].dimension) > 0:
                self._add_container(
                    random.choice(list(Plastic)),
                    random.randint(MIN_CONTAINER_WIDTH, MAX_CONTAINER_WIDTH)
                )

        identification_output = self._user_sorting_function(sensors_output)

        if identification_output is not None:
            for sensor_guid, plastic_type in identification_output.items():
                if sensor_guid in sensed_containers.keys():
                    if sensed_containers[sensor_guid].plastic_type == plastic_type:
                        classified += 1
                    else:
                        mistyped += 1
                    self._containers_list.remove(sensed_containers[sensor_guid])

        return missed, classified, mistyped
