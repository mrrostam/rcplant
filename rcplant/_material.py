from ._dataset import *
from ._types import *

DATA_SETS = dict()
for spectrum in SpectrumType:
    DATA_SETS.update(
        {
            spectrum: Dataset.create(spectrum)
        }
    )


class Material(object):
    def __init__(self, plastic_type: Plastic):
        if not isinstance(plastic_type, Plastic):
            raise ValueError(f'Invalid type of plastic: {plastic_type} \n '
                             f'Supported plastic types: {[e.value for e in Plastic]}')
        self._plastic_type = plastic_type
        self._spectrum = dict()

        for spectrum_type in SpectrumType:
            self._spectrum.update(
                {
                    spectrum_type: DATA_SETS[spectrum_type].get().loc[self._plastic_type.value].sample().iloc[0]
                }
            )

    def spectrum(self, spectrum_type: SpectrumType):
        return self._spectrum[spectrum_type]
