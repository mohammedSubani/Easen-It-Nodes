# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables
flattenedList=IN[0]


# The output to this node will be stored in newList .
newList=[]

for i in flattenedList:
	if isinstance(i,Solid):
		pass
	else:
		newList.append(i)


OUT = newList