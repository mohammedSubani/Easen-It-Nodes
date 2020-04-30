# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
parameters = IN[0]
circleRadius = IN[1]
rotationDegree=IN[2]
height=IN[3]


baseCircle=Circle.ByCenterPointRadius(Point.ByCoordinates(0,0,0),circleRadius)
topCircle=Geometry.Translate(baseCircle,0,0,height)

# Create bottom face points
basePnts=[]
for i in parameters:
	basePnts.append(Curve.PointAtParameter(baseCircle,i))

# Create top face points
topPnts=[]
for i in parameters:
	topPnts.append(Curve.PointAtParameter(topCircle,i))

# Rotate the top face points
rotatedPnts=[]
for i in topPnts:
	rotatedPnts.append(Geometry.Rotate(i,Plane.ByOriginNormal(Point.ByCoordinates(0,0,0),Vector.ByCoordinates(0,0,1)),rotationDegree))

# Make lines between base and rotated points
hyperboloidLines=[]
for i in range(len(rotatedPnts)):
	hyperboloidLines.append(Line.ByStartPointEndPoint(rotatedPnts[i],basePnts[i]))

# Create hyperboloid surface
OUT = Surface.ByLoft(hyperboloidLines,baseCircle)