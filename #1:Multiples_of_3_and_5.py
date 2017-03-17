t=int(raw_input())
while t!=0:
	ans=0
	t-=1
	n=int(raw_input())
	if n>=3:
		n3=int((n-1)/3)
		ans=ans+int((n3*(3+(n3*3)))/2)
	if n>=5:
		n5=int((n-1)/5)
		ans=ans+int((n5*(5+(n5*5)))/2)
	if n>=15:
		n15=int((n-1)/15)
		ans=ans-int((n15*(15+(n15*15)))/2)
	print ans
