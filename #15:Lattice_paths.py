from math import factorial as f
mod=10**9+7
t=int(raw_input())
while t>0:
	t-=1
	n,m=map(int,raw_input().split())
	ans=f(n+m)//f(n)//f(m)
	print ans%mod
