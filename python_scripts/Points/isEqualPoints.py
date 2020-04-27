# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

pnt1=IN[0]
pnt2=IN[1]

if pnt1.X == pnt2.X and pnt1.Y == pnt2.Y and pnt1.Z==pnt2.Z:
	OUT= True
else:
	OUT= False
	
