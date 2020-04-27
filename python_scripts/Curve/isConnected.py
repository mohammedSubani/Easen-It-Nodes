# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
                          
# The inputs to this node will be stored as a list in the IN variables.
crvs = IN[0]
# Tests a list of curves and finds if the curves ar connenected or not
for i in range(1,len(crvs)):
	if Geometry.DistanceTo(crvs[i-1],crvs[i]) !=0:
		OUT=False
		break
	else:
		OUT=True