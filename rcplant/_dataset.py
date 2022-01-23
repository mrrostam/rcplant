import os

import pandas as pd

from ._types import SpectrumType


class Dataset(object):

    def background(self):
        pass

    def get(self):
        pass

    @classmethod
    def create(cls, dataset_type):
        if dataset_type == SpectrumType.FTIR:
            return FTIR()
        elif dataset_type == SpectrumType.Raman:
            return Raman()
        else:
            raise ValueError(f'${dataset_type} is not a valid dataset type, \n'
                             f'Supported dateset types: {[e.value for e in SpectrumType]}')


class FTIR(Dataset):
    def __init__(self):
        data_folder = os.path.join(os.path.dirname(__file__), 'data')
        data_file = os.path.join(data_folder, 'FTIR Plastic Database.xlsx')
        self._data_table = pd.read_excel(data_file, sheet_name=0, index_col=0)
        # it's assumed that the background spectrum is all zeros for now, should be replaced with the actual data
        self._background = self._data_table.loc['background']

    def get(self):
        return self._data_table

    @property
    def background(self):
        return self._background

    def __str__(self):
        return 'FTIR'


class Raman(Dataset):
    def __init__(self):
        data_folder = os.path.join(os.path.dirname(__file__), 'data')
        data_file = os.path.join(data_folder, 'Raman Plastic Database.xlsx')
        self._data_table = pd.read_excel(data_file, sheet_name=0, index_col=0)
        # it's assumed that the background spectrum is all zeros for now, should be replaced with the actual data
        self._background = self._data_table.loc['background']

    def get(self):
        return self._data_table

    @property
    def background(self):
        return self._background

    def __str__(self):
        return 'Raman'
