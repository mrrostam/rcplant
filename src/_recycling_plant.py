import random
import types
from typing import List

from ._constants import *
from ._container import *
from ._conveyor import *
from ._sensor import *
from ._types import SimulationMode


class RecyclingPlant:
    def __init__(
            self,
            sorting_function,
            num_containers: int,
            conveyor: Conveyor,
            sensors: List[Sensor],
            mode: str):
        if not isinstance(sorting_function, types.FunctionType):
            raise ValueError(f'Invalid sorting function, please pass a compatible function')

        if not any(mode == simulation_mode.value for simulation_mode in SimulationMode):
            raise ValueError(f'Invalid simulation mode , \n'
                             f'valid options: {[mode.value for mode in SimulationMode]}')

        if conveyor is None:
            raise ValueError(f'No conveyor is passed')

        if sensors is None:
            raise ValueError(f'No sensor list is passed')

        self._user_sorting_function = sorting_function
        self._mode = mode
        self._conveyor = conveyor
        self._sensors = sensors
        self._num_remaining_containers = num_containers

        self._containers_list = []

        if self._mode == 'training':
            random.seed(1)

    @staticmethod
    def _is_visible_to_sensor(sensor: Sensor, container: Container):
        return container.location.y > sensor.location > (container.location.y - container.dimension.length)

    def _add_container(self, plastic_type: Plastic, dimension: ContainerDimension, location: ContainerLocation):
        self._containers_list.append(Container(plastic_type, dimension, location))

    def _generate_container(self):
        if not self._containers_list or\
                (self._containers_list[-1].location.y - self._containers_list[-1].dimension.length) > \
                random.randint(MIN_CONTAINERS_GAP, MAX_CONTAINERS_GAP):
            self._add_container(
                random.choice(list(Plastic)),
                ContainerDimension(
                    random.randint(MIN_CONTAINER_SIZE, MAX_CONTAINER_SIZE),
                    random.randint(MIN_CONTAINER_SIZE, MAX_CONTAINER_SIZE),
                    random.randint(MIN_CONTAINER_SIZE, MAX_CONTAINER_SIZE),
                ),
                ContainerLocation(INIT_CONTAINER_X, INIT_CONTAINER_Y, INIT_CONTAINER_Z)
            )
            self._num_remaining_containers -= 1

    def update(
            self,
            current_iteration: int,
            simulation_frequency_hz: int,
            sensors_frequency_hz: int):
        missed = 0
        classified = 0
        mistyped = 0
        sensors_output = {}
        sensed_containers = {}

        # init sensor_output with the background spectrum
        for sensor in self._sensors:
            sensors_output.update(
                {
                    sensor.guid: {
                        'type': sensor.type,
                        'location_cm': sensor.location,
                        'spectrum': sensor.read(None, self._mode, sensors_frequency_hz),
                    }
                }
            )

        time_step_sec = 1 / simulation_frequency_hz
        for container in self._containers_list:
            container.location.y += time_step_sec * self._conveyor.speed
            if container.location.y >= self._conveyor.dimension.length:
                self._containers_list.remove(container)
                missed += 1  # container reached the end of the conveyor
            for sensor in self._sensors:
                if self._is_visible_to_sensor(sensor, container):
                    sensors_output.update(
                        {
                            sensor.guid: {
                                'type': sensor.type,
                                'location_cm': sensor.location,
                                'spectrum': sensor.read(container, self._mode, sensors_frequency_hz),
                            }
                        }
                    )
                    sensed_containers.update(
                        {
                            sensor.guid: container
                        }
                    )

        if self._num_remaining_containers != 0:
            self._generate_container()

        identification_output = None
        if current_iteration % (simulation_frequency_hz // sensors_frequency_hz) == 0:
            identification_output = self._user_sorting_function(sensors_output)

        if identification_output is not None:
            for sensor_guid, plastic_type in identification_output.items():
                if sensor_guid in sensed_containers.keys():
                    if sensed_containers[sensor_guid].plastic_type == plastic_type:
                        classified += 1
                    else:
                        mistyped += 1
                    self._containers_list.remove(sensed_containers[sensor_guid])

        is_done = self._num_remaining_containers == 0 and len(self._containers_list) == 0
        return missed, classified, mistyped, is_done
