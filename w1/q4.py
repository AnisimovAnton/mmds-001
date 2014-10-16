def isPrime(n):
    if n < 2: 
         return False;
    if n % 2 == 0:
         return n == 2
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True
		
def map(val):
	res = []
	i = 2
	while i <= val:
		if val % i == 0:
			if isPrime(i):
				res.append((i,val))
		i += 1
	return res

def reduce(vals):
	res = {}
	for pair in vals:
		if pair[0] in res:			
			res[pair[0]] += pair[1]
		else:
			res[pair[0]] = pair[1]
	return res

vals = [15, 21, 24, 30, 49]
inter = []
for i in vals:
	inter.extend(map(i))
#print inter
print reduce(inter)
#res = map(12)
#reduce(res)
#print res