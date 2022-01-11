import uuid

from ._types import ConveyorDimension


class Conveyor:
    def __init__(self, speed_cm_per_second: int, dimension: ConveyorDimension):
        if speed_cm_per_second < 0:
            raise ValueError(f'Invalid speed: {speed_cm_per_second}'
                             f'Conveyor speed should be >= 0 cm per second.')

        if not isinstance(dimension, ConveyorDimension):
            raise ValueError(f'Invalid type of dimension for a conveyor: {dimension}')

        self._speed_cm_per_second = speed_cm_per_second
        self._dimension = dimension
        self._guid = uuid.uuid4()

    @classmethod
    def create(cls, speed_cm_per_second: int, length: int, width: int):
        return Conveyor(
            speed_cm_per_second,
            ConveyorDimension(length, width)
        )

    @property
    def speed(self):
        return self._speed_cm_per_second

    @property
    def dimension(self):
        return self._dimension

    @property
    def guid(self):
        return self._guid.hex

    @speed.setter
    def speed(self, speed_cm_per_second: int):
        if speed_cm_per_second < 0:
            raise ValueError(f'Invalid speed: {speed_cm_per_second} \n'
                             f'Conveyor speed should be >= 0 cm per second.')

        self._speed_cm_per_second = speed_cm_per_second
