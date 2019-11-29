#Solved by Dylan Kriegman on 11/29/2019
def containsOrigin(coords):
	v_01=coords[0]
	v_02=coords[1]
	v_03=coords[2]
	A_013=cross(v_01,v_03)/2
	A_012=cross(v_01,v_02)/2
	A_023=cross(v_02,v_03)/2
	x1,y1,z1=coords[0]
	x2,y2,z2=coords[1]
	x3,y3,z3=coords[2]
	v_12=(x2-x1,y2-y1,0)
	v_13=(x3-x1,y3-y1,0)
	A_123=cross(v_12,v_13)/2
	A_net=A_013+A_012+A_023
	if A_net==A_123:
		return True

def cross(v1,v2):
	a,b,c=v1
	d,e,f=v2
	crossP=((((b*f)-(c*e))**2)+(((c*d)-(a*f))**2)+(((a*e)-(b*d))**2))**0.5
	return crossP

file=open("p102_triangles.txt")
count=0
for line in file:
	coords=[]
	splitLine=line.split(",")
	for i in range(len(splitLine)):
		if i%2==0:
			coords.append((int(splitLine[i]),int(splitLine[i+1]),0))
	if(containsOrigin(coords)):
		count+=1

print(count)
