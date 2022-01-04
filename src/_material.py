from ._dataset import *
from ._types import *
import numpy as np

DATA_SETS = {
    SpectrumType.FTIR: Dataset.create(SpectrumType.FTIR),
    SpectrumType.Raman: Dataset.create(SpectrumType.Raman)
}


class Material(object):
    def __init__(self, plastic_type: Plastic):
        if not isinstance(plastic_type, Plastic):
            raise ValueError(f'Invalid type of plastic for a Container: {plastic_type} \n '
                             f'Supported plastic types: {[e.value for e in Plastic]}')
        self._plastic_type = plastic_type
        self._spectrum = {
            SpectrumType.FTIR: DATA_SETS[SpectrumType.FTIR].get().loc[self._plastic_type.value].sample().iloc[0],
            SpectrumType.Raman: DATA_SETS[SpectrumType.Raman].get().loc[self._plastic_type.value].sample().iloc[0]
        }

    def spectrum(self, spectrum_type: SpectrumType):
        return self._spectrum[spectrum_type]
