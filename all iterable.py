# all iterable
def all(arr):
    for elem in arr:
        if not elem:
            return False
            break
    else:
        return True


a = [1,2,0,4]
if all(a):
    print ("true")
else:
    print ("false")



    
