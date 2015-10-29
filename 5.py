import math

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def isDivisible(num):
	for x in range(11,21):
		if num % x != 0:
			return False
	return True

y = 20
while True:
	if isDivisible(y):
		print(y)
		break
	y = y + 20