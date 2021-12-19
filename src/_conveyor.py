class Conveyor:
    def __init__(self, speed_cm_per_second, length_cm):
        self._speed_cm_per_second = speed_cm_per_second
        self._length_cm = length_cm

    @property
    def speed(self):
        return self._speed_cm_per_second

    @property
    def length(self):
        return self._length_cm
