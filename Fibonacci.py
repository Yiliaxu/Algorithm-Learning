def Loop_Fib(n):
	Fib=[]
	f1=-1
	f2= 1

	while(n>0):
		Fib.append(f1+f2)
		f1,f2=f2,f1+f2
		n-=1
	return Fib

def Recursive_Fib(n):
	if(n <= 1):
		return n
	else:
		return(Recursive_Fib(n-1) + Recursive_Fib(n-2))


if __name__ == '__main__':

	n=10

	Fib = Loop_Fib(n)
	print Fib

	for i in range(n):
		print Recursive_Fib(i),

    




