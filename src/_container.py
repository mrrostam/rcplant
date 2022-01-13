import uuid

from ._material import *
from ._types import *


class Container:
    def __init__(self, plastic_type: Plastic, dimension: ContainerDimension, location: ContainerLocation):
        if not isinstance(plastic_type, Plastic):
            raise ValueError(f'Invalid type of plastic for a Container: {plastic_type} \n '
                             f'Supported plastic types: {[e.value for e in Plastic]}')

        if not isinstance(dimension, ContainerDimension):
            raise ValueError(f'Invalid type of dimension for a Container: {dimension}')

        self._plastic_type = plastic_type
        self._material = Material(plastic_type)
        self._dimension = dimension
        self._location = location
        self._guid = uuid.uuid4()

    @classmethod
    def create(cls, plastic_type: Plastic, length: int, width: int, height: int):
        return Container(
            plastic_type,
            ContainerDimension(length, width, height),
            ContainerLocation(0, 0, 0)
        )

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
