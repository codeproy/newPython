import os
os.chdir(r'E:\Python')
from Array import Array
class Grid(object):

    def __init__(self,rows,columns,value=0):
        self._items = list()
        for elem in Array(rows):
            elem = Array(columns ,value)
            self._items.append(elem)
    #    self._items = Array(rows)
    #    for i in range (rows):
    #        self._items[i] = Array(columns,value)
            
    def getheight(self):
        return(len(self._items))

    def getwidth(self):
        return(len(self._items[0]))

    def setitem(self,r,c,value):

        self._items[r][c] = value
            
    def __str__(self):
        s = ""
        for i in range(self.getheight()):
            for j in range(self.getwidth()):
                s = s + " , " + str(self._items[i][j])
        return (s)

            
            
            
