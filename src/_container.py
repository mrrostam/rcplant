from ._material import *
from ._types import *
import uuid


class Container:
    def __init__(self, plastic_type: Plastic, dimension: ContainerDimension):
        if not isinstance(plastic_type, Plastic):
            raise ValueError(f'Invalid type of plastic for a Container: {plastic_type} \n '
                             f'Supported plastic types: {[e.value for e in Plastic]}')

        if not isinstance(dimension, ContainerDimension):
            raise ValueError(f'Invalid type of dimension for a Container: {dimension}')

        self._plastic_type = plastic_type
        self._material = Material(plastic_type)
        # TODO: change dimension type to support 2d as well
        self._dimension = dimension
        self._location = ContainerLocation(0, 0, 0)
        self._guid = uuid.uuid4()

    @property
    def material(self):
        return self._material

    @property
    def plastic_type(self):
        return self._plastic_type

    @property
    def dimension(self):
        return self._dimension

    @property
    def location(self):
        return self._location

    @property
    def guid(self):
        return self._guid.hex

    @location.setter
    def location(self, new_location: ContainerLocation):
        if not isinstance(new_location, ContainerLocation):
            raise ValueError(f'Invalid type of location for a Container: {new_location}')
        self._location = new_location
