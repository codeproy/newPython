from Node import Node 
class Array2Link(object):
    def __init__(self,arr):
        self.arr = []
        self.arr = arr
        print(self.arr)

    def convert(self):
        self.node1 = None
        j = len(self.arr) - 1
        while ( j != -1):
            self.node1 = Node(self.arr[j],self.node1)
            j = j - 1
        return(self.node1)
            
