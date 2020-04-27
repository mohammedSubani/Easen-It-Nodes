# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
pts=IN[0]

max=pts[0]

for i in pts:
	if i.Y > max.Y:
		max=i

OUT = max