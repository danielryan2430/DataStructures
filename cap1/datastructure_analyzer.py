import sys

class BigOAnalyzer(object):
    def __init__(self, data_structure):
        self._data_structure = data_structure

    @property
    def data_structure(self):
        return self._data_structure

    @data_structure.setter
    def data_structure(self, ds):
        self._data_structure = ds

    # TODO I don't like that this class is directly reading from files.
    # It should take in a list of lines and act accordingly

    def test_insert(self, lines):
        num_lines = len(lines)
        max_steps = 0
        min_steps = sys.maxint
        avg = 0.0
        for l in lines:
            curr = self.data_structure.insert(l)
            max_steps = max(max_steps, curr)
            min_steps = min(min_steps, curr)
            avg = avg + curr
        avg /= num_lines
        return [min_steps, avg, max_steps, num_lines]

    def test_lookup(self, lines):
        num_lines = len(lines)
        max_steps = 0
        min_steps = sys.maxint
        avg = 0.0
        for l in lines:
            curr = self.data_structure.lookup(l)
            max_steps = max(max_steps, curr)
            min_steps = min(min_steps, curr)
            avg = avg + curr
        avg /= num_lines
        return [min_steps, avg, max_steps, num_lines]

    def test_delete(self, lines):
        num_lines = len(lines)
        max_steps = 0
        min_steps = sys.maxint
        avg = 0.0
        for l in lines:
            curr = self.data_structure.delete(l)
            max_steps = max(max_steps, curr)
            min_steps = min(min_steps, curr)
            if curr > 0:
                avg = avg + curr

        avg /= num_lines
        return [min_steps, avg, max_steps, num_lines]
