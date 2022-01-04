import enum


class SpectrumType(enum.Enum):
    FTIR = 'FTIR'
    Raman = 'Raman'


class Plastic(enum.Enum):
    HDPE = 'HDPE'
    LDPE = 'LDPE'
    PP = 'PP'
    PS = 'PS'
    PC = 'PC'
    PVC = 'PVC'
    Polyester = 'Polyester'
    PET = 'PET'
    PU = 'PU'


class SimulationMode(enum.Enum):
    Testing = 'testing'
    Training = 'training'


class ContainerLocation:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @x.setter
    def x(self, new_x):
        self._x = new_x

    @y.setter
    def y(self, new_y):
        self._y = new_y

    @z.setter
    def z(self, new_z):
        self._x = new_z


class ContainerDimension:
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @length.setter
    def length(self, new_length):
        self._length = new_length

    @width.setter
    def width(self, new_width):
        self._width = new_width

    @height.setter
    def height(self, new_height):
        self._height = new_height
