import enum
import os
import pandas as pd


class SpectrumType(enum.Enum):
    FTIR = 'FTIR'
    Raman = 'Raman'


class Dataset(object):
    
    @classmethod
    def create(cls, dataset_type):
        if dataset_type == SpectrumType.FTIR:
            return FTIR()
        elif dataset_type == SpectrumType.Raman:
            return Raman()
        else:
            raise ValueError(f"${dataset_type} is not a valid data type")


class FTIR(Dataset):
    def __init__(self):
        data_folder = os.path.join(os.path.dirname(__file__), 'data')
        data_file = os.path.join(data_folder, 'FTIR Plastic Database.xlsx')
        self._data_table = pd.read_excel(data_file, sheet_name=0, index_col=0)

    def get(self):
        return self._data_table

    def __str__(self):
        return 'FTIR'


class Raman(Dataset):
    def __init__(self):
        data_folder = os.path.join(os.path.dirname(__file__), 'data')
        data_file = os.path.join(data_folder, 'Raman Plastic Database.xlsx')
        self._data_table = pd.read_excel(data_file, sheet_name=0, index_col=0)

    def get(self):
        return self._data_table

    def __str__(self):
        return 'Raman'
