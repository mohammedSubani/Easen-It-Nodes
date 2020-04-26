import clr
import sys
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'

sys.path.append(pyt_path)
import random

# The inputs to this node will be stored as a list in the IN variables.
firstCircle = IN[0]
stoppingRadius= IN[1]
randomRange=IN[2]

# The output to this node will be stored as a list.
result=[]

# A recursive method to create sub-circles.
def replicateCircles(firstCircle):
	# Base Case.
	if Circle.Radius.GetValue(firstCircle) <= stoppingRadius:
		return
	else:
	# Creating sub circle
		newRadius=0.61803398875*Circle.Radius.GetValue(firstCircle)
		centerPoint=Circle.CenterPoint.GetValue(firstCircle)
		newCenter=Geometry.Translate(centerPoint,random.random()*randomRange-randomRange,random.random()*randomRange-randomRange,0)
		newCircle=Circle.ByCenterPointRadius(newCenter,newRadius)
		result.append(newCircle)
		# Calling itself.
		replicateCircles(newCircle)
		
# first call
replicateCircles(firstCircle)


OUT = result
