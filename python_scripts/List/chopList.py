# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
numberOfSublists = IN[0]
lengthsOfSublist = IN[1]
items = IN[2]


# The outputs to this node will be stored as a list in newList.
newList=[]

for i in range(numberOfSublists):
	tmp=[]
	for j in range(lengthsOfSublist):
		try:
			tmp.append(items[i*lengthsOfSublist+j])
		except IndexError:
			break
	newList.append(tmp)
flattened_list = [y for x in newList for y in x]
if len(flattened_list) != len(items):
	raise ValueError('The list has been truncated ! ')


OUT = newList