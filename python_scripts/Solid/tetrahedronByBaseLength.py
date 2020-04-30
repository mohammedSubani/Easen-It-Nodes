# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
import math


# The inputs to this node will be stored as a list in the IN variables.
baseLength = IN[0]

sin60=math.sin(math.radians(60))
basePoints=[]

#Creating Base points of equliteral triangle
basePoints.append(Point.ByCoordinates(0, sin60*baseLength, 0))
basePoints.append(Point.ByCoordinates(-baseLength/2, 0, 0))
basePoints.append(Point.ByCoordinates(baseLength/2, 0, 0))

#Creating the tip of tetrahedron 
baseSurface=Surface.ByPerimeterPoints(basePoints)
basePolygon=Polygon.ByPoints(basePoints)
centerPoint=Polygon.Center(basePolygon)
vertexDirection=Surface.NormalAtPoint(baseSurface,centerPoint)
tipPoint=Geometry.Translate(centerPoint,vertexDirection,((sin60**2)*(baseLength**2)/4)**0.5)

#Creating the thetrahedron surfaces
tetrahedronSrfcs=[]
tetrahedronSrfcs.append(baseSurface)
tetrahedronSrfcs.append(Surface.ByPerimeterPoints([basePoints[0],basePoints[1],tipPoint]))
tetrahedronSrfcs.append(Surface.ByPerimeterPoints([basePoints[0],basePoints[2],tipPoint]))
tetrahedronSrfcs.append(Surface.ByPerimeterPoints([basePoints[1],basePoints[2],tipPoint]))

OUT = tetrahedronSrfcs