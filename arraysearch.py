# Finds missing no. in the integer sequence with max incremental of 1"
def  sumdigit(num):
    array_tbl = list(num)
    a = 1
    for elem in array_tbl:
        if  int(elem) == a:
            pass
        else:
            print(" The missing digit is " , a)
            a = a + 1
        a = a + 1            

rcv = (input("Enter the integer"))
sumdigit(rcv)
