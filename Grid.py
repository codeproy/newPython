import os
os.chdir(r'E:\Python')
from Array import Array
class Grid(object):

    def __init__(self,rows,columns,value=0):
        self._items = Array(rows)
        for i in range (rows):
            self._items[i] = Array(columns,value)
    def getheight(self):
        return(len(self._items))

    def getwidth(self):
        return(len(self._items[0]))
            

   # def __str__(self):
    #    return (str(self._items[len(self._items[0]),len(self._items)]))
            
            
            
