import math
def isPrime(n):
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return False
	return True


def nthPrime(n):
	count=3
	testNum=5
	while count<n:
		testNum+=1
		if isPrime(testNum):
			count+=1
	return testNum
	


total=0
for i in range(2,2000000):
	if isPrime(i):
		total+=i
print(total)