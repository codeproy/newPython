#fibonnaci

def fib(n):
	a = 0
	b = 1 
	l = []
	while a < n:
		l.append(a)
		s = b + a
		a = b
		b = s

	return l
var1 = int(input("enter the no. till fibo "))
k = fib(var1)
print(k)



	
	
