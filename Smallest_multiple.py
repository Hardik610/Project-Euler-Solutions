from fractions import gcd
def lcm(a,b):
	return a//gcd(a,b)*b
t=int(raw_input())
while t!=0:
	t-=1
	n=int(raw_input())
	print reduce(lcm, range(n//2+1, n+1))
