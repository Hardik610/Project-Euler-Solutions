def largest(n):
	i=2
	while i*i<=n:
		if n%i:
			i+=1
		else:
			n //=i
	return n

t=int(raw_input())
while t!=0:
	t-=1
	n=int(raw_input())
	print (largest(n))
