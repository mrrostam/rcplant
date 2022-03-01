import enum

import numpy as np

from ._constants import *
from ._container import Container
from ._material import DATA_SETS
from ._types import SimulationMode
from ._types import SpectrumType


class Sensor:
    _num_sensors = 0

    def __init__(self, sensor_type: SpectrumType, location_cm: int, sensor_id: int = None):
        if location_cm < 0:
            raise ValueError(f'Sensor location should be >= 0.')
        if not isinstance(sensor_type, SpectrumType):
            raise ValueError(f'Invalid type of sensor: {SpectrumType} \n '
                             f'Supported sensors types: {[e.value for e in SpectrumType]}')

        self._location_cm = location_cm
        self._sensor_type = sensor_type
        self._background_spectrum = DATA_SETS[self._sensor_type].background

        if sensor_id is None:
            Sensor._num_sensors += 1
            self._id = Sensor._num_sensors
        else:
            self._id = sensor_id

    @classmethod
    def reset_num(cls):
        cls._num_sensors = 0

    @classmethod
    def create(cls, sensor_type: SpectrumType, location: int, sensor_id: int = None):
        return Sensor(sensor_type, location, sensor_id)

    @property
    def location(self):
        return self._location_cm

    @property
    def type(self):
        return self._sensor_type

    @property
    def id(self):
        return self._id

    def read(self, container: Container, mode: str, sampling_frequency: int):
        if container is None:
            raw_output = self._background_spectrum
        else:
            raw_output = container.material.spectrum(self._sensor_type)

        if mode == SimulationMode.Training.value:
            return raw_output
        elif mode == SimulationMode.Testing.value:
            signal_power = raw_output ** 2
            signal_average_power = np.mean(signal_power)
            signal_average_power_db = 10 * np.log10(signal_average_power + EPSILON_POWER)
            noise_average_power_db = signal_average_power_db - SAMPLING_FREQUENCY_TO_SNR_DB[sampling_frequency]
            noise_average_power = 10 ** (noise_average_power_db / 10)
            noise = np.absolute(np.random.normal(NOISE_MU_VALUE, np.sqrt(noise_average_power), raw_output.size))
            return (raw_output + noise).rename("unknown_plastic")
        else:
            raise ValueError(f'Invalid reading mode,\n'
                             f'valid options: {[mode.value for mode in SimulationMode]}')
