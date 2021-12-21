import enum
import uuid

from ._enums import SpectrumType
from ._material import DATA_SETS
from ._container import Container
from ._enums import SimulationMode

NOISE_MU_VALUE = 0
NOISE_SIGMA_VALUE = 0.1


class Sensor:
    def __init__(self, location_cm: int, sensor_type: SpectrumType):
        if location_cm < 0:
            raise ValueError(f'Sensor location should be >= 0.')
        self._location_cm = location_cm
        if not isinstance(sensor_type, SpectrumType):
            raise ValueError(f'Invalid type of sensor: {SpectrumType} \n '
                             f'Supported sensors types: {[e.value for e in SpectrumType]}')
        self._sensor_type = sensor_type
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
            raw_output = DATA_SETS[self._sensor_type].background
        else:
            raw_output = container.material.spectrum(self._sensor_type)

        if mode == SimulationMode.Training.value:
            return raw_output
        elif mode == SimulationMode.Testing.value:
            noise = np.random.normal(NOISE_MU_VALUE, NOISE_SIGMA_VALUE, raw_output.size)
            return raw_output + noise
        else:
            raise ValueError(f'Invalid reading mode,\n'
                             f'valid options: {[mode.value for mode in SimulationMode]}')