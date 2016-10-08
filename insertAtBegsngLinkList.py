import os
os.chdir(r'E:\Python')
from Array import Array
from Node import Node
from Array2Link import Array2Link
from replaceLinkList import replaceLinkList
def insertAtbeg(head,data):
    if (head == None):
        head = Node(data)
        head.nexti = None
    else:
        head =  Node(data, head)
    return(head)
        
a1 = Array(20,5)
a1[3] = 20
a1[6] = 55
a1n = Array2Link(a1)
a1h = a1n.convert()
print('data ', a1h.data)
a1h = insertAtbeg(a1h, 222)
while(a1h != None):
    print(a1h.data)
    a1h = a1h.nexti

