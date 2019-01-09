#Solved by Dylan Kriegman on 1/9/2019
def getSumOfDivisors(num):
	divisors=[]
	for potentialDivisor in range(1,num):
		if num%potentialDivisor==0:
			divisors.append(potentialDivisor)
	return sum(divisors)

def isAmicable(num):
	if getSumOfDivisors(getSumOfDivisors(num))==num and getSumOfDivisors(num)!=num:
		return True
	return False

#Returns the sum of all amicable numbers under 10000
def getSumOfAmicableNumbers():
	total=0
	for i in range(1,10000):
		if isAmicable(i):
			total+=i
	return total
print(str(getSumOfAmicableNumbers()))
