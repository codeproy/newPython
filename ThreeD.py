import os
os.chdir(r'E:\Python')
from Array import Array
from Grid import Grid

class Threed(object):
    def __init__(self,rows,columns,height,value=0):
        self._items = list()
        for elem in Array(rows):
            elem = Grid(columns, height ,value)
            self._items.append(elem)

    def getheight(self):
        return(len(self._items))

    def getwidth(self):
        return(len(self._items[0]))

    def getdepth(self):
        return(len(self._items[0][0]))
