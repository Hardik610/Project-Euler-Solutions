def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n//2) if sieve[i]]

ans=prime_sieve(10000000)
t=int(raw_input())
while t>0:
	t-=1
	n=int(raw_input())
	print ans[n-1]
