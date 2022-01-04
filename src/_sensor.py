import enum
import uuid

import numpy as np

from ._container import Container
from ._material import DATA_SETS
from ._types import SimulationMode
from ._types import SpectrumType

SNR_DB = 20
NOISE_MU_VALUE = 0
EPSILON_POWER = 0.0001


class Sensor:
    def __init__(self, location_cm: int, sensor_type: SpectrumType):
        if location_cm < 0:
            raise ValueError(f'Sensor location should be >= 0.')
        self._location_cm = location_cm
        if not isinstance(sensor_type, SpectrumType):
            raise ValueError(f'Invalid type of sensor: {SpectrumType} \n '
                             f'Supported sensors types: {[e.value for e in SpectrumType]}')
        self._sensor_type = sensor_type
        self._background_spectrum = DATA_SETS[self._sensor_type].background
        self._guid = uuid.uuid4()

    @property
    def location(self):
        return self._location_cm

    @property
    def type(self):
        return self._sensor_type

    @property
    def guid(self):
        return self._guid.hex

    def read(self, container: Container, mode: SimulationMode):
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
            noise_average_power_db = signal_average_power_db - SNR_DB
            noise_average_power = 10 ** (noise_average_power_db / 10)
            noise = np.random.normal(NOISE_MU_VALUE, np.sqrt(noise_average_power), raw_output.size)
            if raw_output.name != 'background':
                print(noise)
                print(raw_output)
                print(raw_output + noise)
                input()
            return raw_output + noise
        else:
            raise ValueError(f'Invalid reading mode,\n'
                             f'valid options: {[mode.value for mode in SimulationMode]}')
