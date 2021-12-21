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
