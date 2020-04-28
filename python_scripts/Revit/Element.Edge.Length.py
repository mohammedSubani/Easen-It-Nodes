import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *


elems = IN[0]
lengths=[]

for i in elems:
	lengths.append(Curve.Length.GetValue(i))
	
OUT = lengths,sum(lengths)
