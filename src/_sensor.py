import enum
from _dataset import SpectrumType


class Sensor:
    def __init__(self, location_cm, sensor_type):
        self._location_cm = location_cm
        self._sensor_type = sensor_type

    @property
    def location(self):
        return self._location_cm

    @property
    def type(self):
        return self._sensor_type

    def read(self, container):
        return container.material.spectrum(self._sensor_type)
