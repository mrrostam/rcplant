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
    Blank = 'background'


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
        if length <= 0:
            raise ValueError(f'Invalid value for length: {length}; should be > 0.')
        if width <= 0:
            raise ValueError(f'Invalid value for width: {width}; should be > 0.')
        if height <= 0:
            raise ValueError(f'Invalid value for height: {height}; should be > 0.')

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
        if new_length <= 0:
            raise ValueError(f'Invalid value for length: {new_length}; should be > 0.')
        self._length = new_length

    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            raise ValueError(f'Invalid value for width: {new_width}; should be > 0.')
        self._width = new_width

    @height.setter
    def height(self, new_height):
        if new_height <= 0:
            raise ValueError(f'Invalid value for height: {new_height}; should be > 0.')
        self._height = new_height


class ConveyorDimension:
    def __init__(self, length, width):
        if length <= 0:
            raise ValueError(f'Invalid value for length: {length}; should be > 0.')
        if width <= 0:
            raise ValueError(f'Invalid value for width: {width}; should be > 0.')
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, new_length):
        if new_length <= 0:
            raise ValueError(f'Invalid value for length: {new_length}; should be > 0.')
        self._length = new_length

    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            raise ValueError(f'Invalid value for width: {new_width}; should be > 0.')
        self._width = new_width
