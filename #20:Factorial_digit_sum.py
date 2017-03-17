from math import factorial
t=int(raw_input())
while t>0:
	t-=1
	summ=0
	n=int(raw_input())
	fac=factorial(n)
	f=str(fac)
	for i in f:
		summ+=int(i)
	print summ
