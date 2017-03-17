t=int(raw_input())
while t>0:
	t-=1
	ans=0
	n=int(raw_input())
	po=2**n
	po=str(po)
	for i in (po):
		ans+=int(i)
	print ans
