def getFactorial(n):
	if n>1:
		return n*getFactorial(n-1)
	elif n==0:
		return 1
	return n

factorials=dict()
for i in range(0,10):
	factorials[i]=getFactorial(i)

def getSumOfDigitsFactorial(n):
	n=str(n)
	total=0
	for i in range(len(n)):
		total+=factorials[int(n[i])]
	return total

total=0
nums=[]
for i in range(3,2540160+1):
	if(getSumOfDigitsFactorial(i)==i):
		total+=i
		nums.append(i)
print(total)
print(nums)
