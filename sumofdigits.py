# Sum of digits of an integer
import os
import glob
not_found = True
a = ['10 A OLD' , '10 A NEW' , '20 B OLD' , '20 B NEW']
b = ['A' , 'B']
j = 0
for i in range(0 , len(b)):
    not_found = True
    while not_found:
        if b[i] in a[j]:
            if 'OLD' in a[j]:
                 print (b[i])
            not_found = False
        else:
             j = j + 1
            

    
