import uuid


class Conveyor:
    def __init__(self, speed_cm_per_second: int, length_cm: int):
        if speed_cm_per_second < 0:
            raise ValueError(f'Invalid speed: {speed_cm_per_second}'
                             f'Conveyor speed should be >= 0 cm per second.')
        if length_cm < 0:
            raise ValueError(f'Invalid length: {length_cm}'
                             f'Conveyor length should be >= 0 cm.')

        self._speed_cm_per_second = speed_cm_per_second
        self._length_cm = length_cm
        self._guid = uuid.uuid4()

    @property
    def speed(self):
        return self._speed_cm_per_second

    @property
    def length(self):
        return self._length_cm

    @property
    def guid(self):
        return self._guid.hex

    @speed.setter
    def speed(self, speed_cm_per_second: int):
        if speed_cm_per_second < 0:
            raise ValueError(f'Invalid speed: {speed_cm_per_second} \n'
                             f'Conveyor speed should be >= 0 cm per second.')
        
        self._speed_cm_per_second = speed_cm_per_second
