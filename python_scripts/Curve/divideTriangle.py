# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
triangle = IN[0]
stopLength = IN[1]
# The output lists that will eventually going to be stored in the OUT variable.
result=[]

# A recrusive method that will iterat over sub-traingles until it reaches a certain length that will return all of the sub traingles
def iterateTriangle(triangle):
###
# Finding the new points for the new sub-traingles
	crvs=Polygon.Curves(triangle)
	triCorners=Polygon.Corners(triangle)
	centerPnts=[]
	for i in crvs:
		centerPnts.append(Curve.PointAtParameter(i,0.5))

# Creating sub-traingles
	tris=[]
	tris.append(Polygon.ByPoints([centerPnts[0],centerPnts[1],centerPnts[2]]))
	tris.append(Polygon.ByPoints([centerPnts[0],centerPnts[1],triCorners[1]]))
	tris.append(Polygon.ByPoints([centerPnts[1],centerPnts[2],triCorners[2]]))
	tris.append(Polygon.ByPoints([centerPnts[0],centerPnts[2],triCorners[0]]))

# Adding sub-traingles to output list
	pCrvs=Polygon.Curves(tris[0])
	if Curve.Length.GetValue(pCrvs[0]) < stopLength:
		result.append(tris)
		return
	else:
		for i in tris:
			iterateTriangle(i)
# Calling iterateTriangle method for multiple input triangles			
for i in triangle:
	iterateTriangle(i)

OUT = result