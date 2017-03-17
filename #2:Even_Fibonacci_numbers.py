t=int(raw_input())
while t!=0:
	t-=1
	t1=1
	t2=2
	count=2
	n=int(raw_input())
	if n==2:
		ans=2
	elif n==1:
		ans=0
	else:
		ans=2
		summ=0
		while t2<n:
			summ=t1+t2
			#print summ
			t1=t2
			#print t1
			t2=summ
			if t2>n:
				break
			if (t2%2)==0:
				ans=ans+t2
	print ans
