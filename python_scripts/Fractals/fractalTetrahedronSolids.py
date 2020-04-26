# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

import math

# The inputs to this node will be stored as a list in the IN variables.
baseLength = IN[0]
stopArea = IN[1]
# A constant to be used.
sin60=math.sin(math.radians(60))

# The output to this node will be stored as a list in these list variables.

result=[]
basePoints=[]

#Creating first base points of equliteral triangle located using globals cs

basePoints.append(Point.ByCoordinates(0, sin60*baseLength, 0))
basePoints.append(Point.ByCoordinates(-baseLength/2, 0, 0))
basePoints.append(Point.ByCoordinates(baseLength/2, 0, 0))

# A method to create the fractals the recursion ends if the given surface area is larger the one given in the method.
def tetrahedronFractals(basePoints):
	#Creating the tip of tetrahedron
	baseLength=Geometry.DistanceTo(basePoints[0],basePoints[1])
	baseSurface=Surface.ByPerimeterPoints(basePoints)
	basePolygon=Polygon.ByPoints(basePoints)
	centerPoint=Polygon.Center(basePolygon)
	vertexDirection=Surface.NormalAtPoint(baseSurface,centerPoint)
	tipPoint=Geometry.Translate(centerPoint,vertexDirection,((sin60**2)*(baseLength**2)/4)**0.5)
    

	#Creating the thetrahedron surfaces
    
	tetrahedronSrfcs=[]
	tetrahedronSrfcs.append(baseSurface)
	tetrahedronSrfcs.append(Surface.ByPerimeterPoints([basePoints[0],basePoints[1],tipPoint]))
	tetrahedronSrfcs.append(Surface.ByPerimeterPoints([basePoints[2],basePoints[0],tipPoint]))
	tetrahedronSrfcs.append(Surface.ByPerimeterPoints([basePoints[1],basePoints[2],tipPoint]))
    
	#Appending the solid geometry result of the tetrahedron
    
	result.append(Solid.ByJoinedSurfaces(tetrahedronSrfcs))
    
	#Creating the recursion fro fractals
    
	if Surface.Area.GetValue(baseSurface) < stopArea: #Base case
		return
	else:                                      #Recursion statement
		for i in tetrahedronSrfcs:
			faceCurves=Surface.PerimeterCurves(i)
			newBasePoints=[]
			for j in faceCurves:
				newBasePoints.append(Curve.PointAtParameter(j,0.5))
			tetrahedronFractals(newBasePoints)



tetrahedronFractals(basePoints)

OUT = result