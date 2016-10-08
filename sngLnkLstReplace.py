import os
os.chdir(r'E:\Python')
from Array import Array
from Node import Node
from Array2Link import Array2Link
from replaceLinkList import replaceLinkList
a1 = Array(20,5)
a1[3] = 20
a1[6] = 55
a1n = Array2Link(a1)
a1h = a1n.convert()
print('data ', a1h.data)
a1h = replaceLinkList(a1h,5,-33)
while (a1h != None):
    print(a1h.data)
    a1h = a1h.nexti

