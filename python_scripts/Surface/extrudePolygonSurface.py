# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
polygonList=IN[0]
extrudedPoint=IN[1]


tmp=[]
try:
	polygon=[]
	for j in polygonList:
		polygon.append(j)
	tmp.append(Polygon.Corners(polygon[0]))
except TypeError as t:
	tmp.append(Polygon.Corners(polygonList))
	
tmpPnt=[]
try:
	exPoint=[]
	for j in extrudedPoint:
		exPoint.append(j)
	tmpPnt.append(exPoint[0])
except TypeError as t:
	tmpPnt.append(extrudedPoint)
	
polygonCorners=tmp[0]
extrudedPoint=tmpPnt[0]

srfcs=[]

for i in range(0,len(polygonCorners)):
	tmpPnts=[]
	tmpPnts.append(polygonCorners[i-1])
	tmpPnts.append(polygonCorners[i])
	tmpPnts.append(extrudedPoint)
	srfcs.append(Surface.ByPerimeterPoints(tmpPnts))

OUT = srfcs