import os
os.chdir(r'E:\Python')
from Array import Array
from Node import Node
from Array2Link import Array2Link
from replaceLinkList import replaceLinkList
def insertAtend(head,data):
    shead = head
    if (head == None):
        head = Node(data)
        head.nexti = None
    else:
        while (head.nexti != None):
            head = head.nexti
        head.nexti = Node(data)
    return(shead)
        
a1 = Array(10,5)
a1[3] = 20
a1[6] = 55
a1n = Array2Link(a1)
a1h = a1n.convert()
print('data ', a1h.data)
a1h = insertAtend(a1h, 222)
while(a1h != None):
    print(a1h.data)
    a1h = a1h.nexti
