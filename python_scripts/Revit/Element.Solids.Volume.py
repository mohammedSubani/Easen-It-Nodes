# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')

from Autodesk.DesignScript.Geometry import *


# The inputs to this node will be stored as a list in the IN variables.
elements = IN[0]

solids=[]
solidVol=[]
solids.append(elements.Geometry())
for i in solids:
	for j in i:
		solidVol.append(round(Solid.Volume.GetValue(j),3))
		
	
OUT = solidVol,sum(solidVol)