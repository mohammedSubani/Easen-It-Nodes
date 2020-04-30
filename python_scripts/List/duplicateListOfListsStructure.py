import clr
import sys
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)


input_list=IN[0]


# A recursive method that moves at all levels and create list for each level .
def createListStructure(inputList) :
	listCounter =0
	for i in inputList:
		if isinstance(i, list) :
			listCounter +=1
	if listCounter ==0:
		return []
	tmp=[] 
	for i in inputList:
		if isinstance(i, list) :
			tmp.append(createListStructure(i))
	return tmp
 
# Calling the method and assign it as output .
OUT=createListStructure(input_list)