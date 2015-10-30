#A pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
#There exists exactly one pythagorean triplet for which a + b + c = 1000

for x in range(1,333):
	for y in range(2,500):
		z = 1000 - x - y
		if x**2+y**2 == z**2:
			print(x*y*z)