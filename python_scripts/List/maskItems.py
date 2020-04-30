# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
listOfLists = IN[0]

# The output to this node will be stored in result.
result=[]

maxLength=0
for i in range(len(listOfLists)):

	if len(listOfLists[i])>maxLength:
		maxLength=len(listOfLists[i])

for i in range(maxLength):
	try:
		tmp=[]
		for j in range(len(listOfLists)):
			tmp.append(listOfLists[j][i])
	except IndexError :
		tmp.append(None)
	result.append(tmp)
	
	
OUT = result
