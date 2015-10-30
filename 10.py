#Find the sum of all primes below two million

def isPrime(num):
	for i in range(2,int(num**0.5)+1):
		if num%i==0:
			return False
	return True

sum = 0
for x in range(2,2000001):
	if isPrime(x):
		sum = sum + x
print sum