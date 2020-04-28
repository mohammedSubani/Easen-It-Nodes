import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

srfcs = IN[0]
areas=[]

for i in srfcs:
	areas.append(round(Surface.Area.GetValue(i),3))

OUT = areas,sum(areas)