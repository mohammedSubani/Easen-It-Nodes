import clr
import sys
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import json

import json
input_list=IN[0]

def parseJSON(inputList) :
	listCounter =0
	for i in inputList:
		if isinstance(i, list) :
			listCounter +=1
	if listCounter ==0:
		tmp=[] 
		for i in inputList:
			tmp.append(str(i)) 
		return tmp
		
	tmp=[] 
	for i in inputList:
		if isinstance(i, list) :
			tmp.append(parseJSON(i))
		else:
			tmp.append(i)
	return tmp
 

OUT=json.dumps(parseJSON(input_list))