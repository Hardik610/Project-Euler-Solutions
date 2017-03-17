t=int(raw_input())
while t>0:
	t-=1
	n=int(raw_input())
	ans=((n*(n+1))/2)**2-((n*(n+1)*(2*n+1))/6)
	print ans
