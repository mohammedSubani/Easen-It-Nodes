import clr
import sys
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import random

# the inputs to this list.
listOfItems = IN[0]
numberOfItems = IN[1]

# The outputs stored in pickedItems.
pickedItems=[]

for i in range(numberOfItems):
	randomIndex=int(random.random()*len(listOfItems))
	pickedItems.append(listOfItems[randomIndex])


OUT = pickedItems