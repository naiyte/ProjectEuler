#First six primes are 2, 3, 5, 7, 11, and 13
#What is the 10,001st prime number

def isPrime(num):
	for i in range(2,int(num**0.5)+1):
		if num%i==0:
			return False
	return True

count = 0
num = 1
while count < 10001:
	num = num + 1
	if isPrime(num):
		count = count + 1
print(num)