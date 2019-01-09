#Solved by Dylan Kriegman on 1/9/2019
def factorial(n):
	if n==1:
		return 1
	return n*factorial(n-1)

num=str(factorial(100))
total=0
for digit in num:
	total+=int(digit)
print(str(total))
