# to find a prime no
def primefunc(a,b):
    for i in range(a,b):
        for j in range (2,i):
            if (i % j == 0) :
                print ("the number is not prime" , i )
                break
        else:
            print ("the number is prime", i)

num1 = int(input("enter the 1st "))
num2 = int(input("enter the 2nd "))
primefunc(num1,num2)
    
