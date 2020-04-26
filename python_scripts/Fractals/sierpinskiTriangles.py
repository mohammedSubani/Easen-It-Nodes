# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
import math
# The inputs to this node will be stored as a list in the IN variables.
length = IN[0]
stopLength=IN[1]
sin60=math.sin(math.radians(60))

# Creating the first triangle.
pnts=[]
pnts.append(Point.ByCoordinates(-length/2,0,0))
pnts.append(Point.ByCoordinates(length/2,0,0))
pnts.append(Point.ByCoordinates(0,sin60*length,0))

# The output to this node will be stored as a list in the IN variables.
result=[]

# A recursive method to create sub-triangles.
def creatSubTriangles(eqTri):
	# Getting the curves of the triangle .
	crvs=PolyCurve.Curves(eqTri)
	# Getting the corners for the triangle .
	startPnts=[]
	for i in crvs:
		startPnts.append(Curve.StartPoint.GetValue(i))
	# Getting the mid points for the triangle .
	newPnts=[]
	for i in crvs:
		newPnts.append(Curve.PointAtParameter(i,0.5))
	# Creating sub-triangles .
	resultTriangles=[]
	resultTriangles.append(Polygon.ByPoints(newPnts))
	resultTriangles.append(Polygon.ByPoints([startPnts[0],newPnts[0],newPnts[2]]))
	resultTriangles.append(Polygon.ByPoints([startPnts[1],newPnts[0],newPnts[1]]))
	resultTriangles.append(Polygon.ByPoints([startPnts[2],newPnts[1],newPnts[2]]))
	# Base Case.
	if Curve.Length.GetValue(crvs[0])<stopLength:
		return
	result.append(resultTriangles[0])
	for i in range(1,len(resultTriangles)):
		creatSubTriangles(resultTriangles[i])

# Create first triangle store it and pass it to the method .
triPolygon=Polygon.ByPoints(pnts)
result.append(triPolygon)
# First call .
creatSubTriangles(triPolygon)


OUT = result

