# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
firstList  =IN[0]
secondList =IN[1]

# The output to this node will be stored in newList.
newList=[]

assert len(firstList)==len(secondList),'lists are not of equal length'

for i in range(len(firstList)):
	tmp=[]
	tmp.append(firstList[i])
	tmp.append(secondList[i])
	newList.append(tmp)


OUT = newList