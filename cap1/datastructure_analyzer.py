import os


class BigOAnalyzer(object):
    def __init__(self, data_structure):
        self.data_structure = data_structure

    @property
    def data_structure(self):
        return self._data_structure

    @data_structure.setter
    def data_structure(self, ds):
        self._data_structure = ds

    def test_input(self,path):
        file = os.open(path)
        for i in file.getLines():
            self.data_structure.insert(i)



