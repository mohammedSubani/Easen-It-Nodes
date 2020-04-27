# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
crv = IN[0]
# Test the input curve if it is a line or not boolean return value
def isLine(curve):
	sPnt=Curve.StartPoint.GetValue(curve)
	ePnt=Curve.EndPoint.GetValue(curve)
	
	if round(Curve.Length.GetValue(curve),3) == round(Geometry.DistanceTo(sPnt,ePnt),3):
		return True
	else:
		return False
	
OUT = isLine(crv)

