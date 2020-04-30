# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
listToFilter = IN[0]

filteredList=[]

for i in range(len(listToFilter)):
	if i % 2 == 0 :
		filteredList.Add(listToFilter[i])
OUT = filteredList