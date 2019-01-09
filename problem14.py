#Solved on 8/1/2019 by Dylan Kriegman
def getChainLength(knownChainLengths,number,iteration):
	if number==1:
		return iteration
	elif number in knownChainLengths:
		return knownChainLengths[number]+iteration
	elif number%2==0:
		return getChainLength(knownChainLengths,number//2,iteration+1)
	else:
		return getChainLength(knownChainLengths,(3*number)+1,iteration+1)

longestChainLength=0
numberWithLongestChainLength=None
knownChainLengths=dict()
for potentialNumber in range(1,1000000):
	currentChainLength=getChainLength(knownChainLengths,potentialNumber,1)
	knownChainLengths[potentialNumber]=currentChainLength
	if currentChainLength>longestChainLength:
		longestChainLength=currentChainLength
		numberWithLongestChainLength=potentialNumber
print("numberWithLongestChainLength: "+str(numberWithLongestChainLength))	

		
