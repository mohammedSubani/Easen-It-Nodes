# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
pts=IN[0]

min=pts[0]

for i in pts:
	if i.Y < min.Y:
		min=i

OUT = min
