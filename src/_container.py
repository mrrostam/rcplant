from _material import *


class Container:
    def __init__(self, plastic_type, dimension_cm):
        self._plastic_type = plastic_type
        self._material = Material(plastic_type)
        self._dimension_cm = dimension_cm
        self._position_cm = 0

    @property
    def material(self):
        return self._material

    @property
    def plastic_type(self):
        return self._plastic_type

    @property
    def dimension(self):
        return self._dimension_cm

    @property
    def position(self):
        return self._position_cm

    @position.setter
    def position(self, new_position_cm):
        self._position_cm = new_position_cm
