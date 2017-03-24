class DataStructureBase(object):
    def insert(self, value):
        raise NotImplementedError()

    def lookup(self,value):
        raise NotImplementedError()

    def delete(self,value):
        raise NotImplementedError()
