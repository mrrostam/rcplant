import enum
from _dataset import Dataset
from _dataset import SpectrumType

data_sets = {
    SpectrumType.FTIR: Dataset.create(SpectrumType.FTIR),
    SpectrumType.Raman: Dataset.create(SpectrumType.Raman)
}


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


class Material(object):
    def __init__(self, plastic_type):
        self._plastic_type = plastic_type
        self._spectrum = {
            SpectrumType.FTIR: data_sets[SpectrumType.FTIR].get().loc[self._plastic_type.value].sample(),
            SpectrumType.Raman: data_sets[SpectrumType.Raman].get().loc[self._plastic_type.value].sample()
        }

    def spectrum(self, type: SpectrumType):
        return self._spectrum[type]
