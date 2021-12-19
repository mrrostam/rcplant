from _container import *
from _conveyor import *
from _sensor import *
import random

DEFAULT_CONVEYOR_POSITION = 1000
DEFAULT_CONVEYOR_SPEED = 1
DEFAULT_SENSOR_POSITION = 500
DEFAULT_SENSOR_TYPE = SpectrumType.FTIR


class RecyclingPlant:
    def __init__(self, sorting_function, conveyor=None, sensors=None):
        self._user_sorting_function = sorting_function
        if conveyor is None:
            self._conveyor = Conveyor(DEFAULT_CONVEYOR_SPEED, DEFAULT_CONVEYOR_POSITION)
        else:
            self._conveyor = conveyor

        if sensors is None:
            self._sensor = Sensor(DEFAULT_SENSOR_POSITION, DEFAULT_SENSOR_TYPE)
        else:
            self._sensor = sensors

        self._containers_list = []

    def add_container(self, plastic_type, dimension):
        self._containers_list.append(Container(plastic_type, dimension))

    def update(self, time_step, enable):
        missed = 0
        classified = 0
        mistyped = 0
        sensor_output = None
        sensed_container = None

        for container in self._containers_list:
            container.position += time_step * self._conveyor.speed
            if container.position >= self._conveyor.length:
                self._containers_list.remove(container)
                missed += 1
            if container.position > self._sensor.location > (container.position - container.dimension):
                sensor_output = self._sensor.read(container)
                sensed_container = container

        if random.random() > 0.5 and enable:
            if not self._containers_list or (self._containers_list[-1].position - self._containers_list[-1].dimension) > 0:
                self.add_container(random.choice(list(Plastic)), random.randint(7, 15))

        identification_output = self._user_sorting_function(sensor_output)
        if sensed_container is not None and identification_output is not None:
            if sensed_container.plastic_type == identification_output:
                classified += 1
            else:
                mistyped += 1
            self._containers_list.remove(sensed_container)

        return missed, classified, mistyped
