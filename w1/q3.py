a = 1.0
b = 1.0
c = 1.0
for i in range(5):
	a1 = c
	b1 = a / 2.0
	c1 = a / 2.0 + b
	a = a1
	b = b1
	c = c1
	print a, b, c
print a, b, c