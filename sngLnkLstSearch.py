import os
os.chdir(r'E:\Python')
from Array import Array
from Node import Node
from Array2Link import Array2Link
from searchLink import searchLinkList
a1 = Array(20,5)
a1[3] = 20
a1[6] = 55
a1n = Array2Link(a1)
a1h = a1n.convert()
print('data ', a1h.data)
print (searchLinkList(a1h, -33))

