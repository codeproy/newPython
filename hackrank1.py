#!/usr/bin/py
# Head ends here
def lonelyinteger(n,a):
    input_no_elem = n
    elem_table = []
    elem_table = list(a)
    max_elem = 0  # maximum no. of ocuuernce
    count_elem = 0 # sum of occurences

    for i in range(0,input_no_elem):
           srch_elem = elem_table[i]
           count_elem = 0
        
           for j in range(0, input_no_elem):
                   if srch_elem == elem_table[j]:   
                           count_elem = count_elem + 1
                           if count_elem == 2:
                               break
                               
           else:
              return srch_elem

N = int(input())
A = input().split(" ")
print(lonelyinteger(N,A))
