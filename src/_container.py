from ._material import *
import uuid


class Container:
    def __init__(self, plastic_type: Plastic, dimension_cm: int):
        if not isinstance(plastic_type, Plastic):
            raise ValueError(f'Invalid type of plastic for a Container: {plastic_type} \n '
                             f'Supported plastic types: {[e.value for e in Plastic]}')

        if dimension_cm < 1:
            raise ValueError(f'Invalid container size: {dimension_cm} \n '
                             f'Container width should be >= 1 cm.')

        self._plastic_type = plastic_type
        self._material = Material(plastic_type)
        # TODO: change dimension type to support 2d as well
        self._dimension_cm = dimension_cm
        self._location_cm = 0
        self._guid = uuid.uuid4()

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
    def location(self):
        return self._location_cm

    @property
    def guid(self):
        return self._guid.hex

    @location.setter
    def location(self, new_location_cm: int):
        if new_location_cm < 0:
            raise ValueError(f'Invalid location: {new_location_cm} \n '
                             f'Container location should be >= 0.')
        self._location_cm = new_location_cm
