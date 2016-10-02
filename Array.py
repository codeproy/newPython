class Array(object):
    def __init__(self,size,value=0):
        self._items = list()
        for i in range(0,size):
            self._items.append(value)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return (str(self._items))

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self,index):
         return self._items[index]

    def __setitem__(self,index, ivalue):
        self._items[index] = ivalue

    def insert(self,index,ivalue):
        self._intm = []
        for i in range(0,index-1):
            self._intm.append(self._items[i])
        self._intm.append(ivalue)
        for i in range(index-1,len(self._items)):
            self._intm.append(self._items[i])
        self._items = self._intm

    
         
