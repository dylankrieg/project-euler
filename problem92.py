def getSumOfSquares(num):
    sum=0
    numDigits=len(str(num))
    for i in range(0,numDigits):
        sum+=(num%10)**2
	num//=10
    return sum

def convergesToOne(num,oneConvergences,eightyNineConvergences):
    if num in oneConvergences:
        return True
    elif num in eightyNineConvergences:
        return False
    while num!=1 and num!=89:
        num=getSumOfSquares(num)
    if num==1:
	return True
    return False

def getNumberOfEightyNineConvergences():
    numberOfConvergencesToEightyNine=0
    oneConvergences=set()
    eightyNineConvergences=set()
    for potentialNum in range(1,10000000):
        if convergesToOne(potentialNum,oneConvergences,eightyNineConvergences):
            oneConvergences.add(potentialNum)
        else:
	    eightyNineConvergences.add(potentialNum)
     	    numberOfConvergencesToEightyNine+=1
        #print(potentialNum)
        print(len(oneConvergences))
	print(len(eightyNineConvergences))
    return numberOfConvergencesToEightyNine       
	
	
print("This is the Sum of Squares Test")
print(str(getSumOfSquares(3))) 
print("Testing converges to one")
print(str(convergesToOne(145,set([1]),set([2]))))
numsThatConvergeToOne=set()

print(str(getNumberOfEightyNineConvergences())+" numbers converge to 89")
