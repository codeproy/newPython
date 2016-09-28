# decimal to binary convesion, flipping the bits & throwing the decimal value)
def  maxxor(num1 , num2):
    if num1 < num2:
        pass
    else:
        intr  = num1
        num1  = num2
        num2 = intr    
    xsum = 0
    maxs = 0 
    for i in range(num1 , num2 + 1):
        j = i
        while j < num2 + 1:
            xsum = i ^ j
            if xsum > maxs:
                maxs = xsum
            j = j + 1
    return(maxs)
            
pnum1 = int(input())
pnum2 = int(input())
print(maxxor(pnum1 , pnum2))    
