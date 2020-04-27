import clr
import sys
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# A method that measures the distance between two points .
def distance(pnt1,pnt2):
	return (((pnt2.X-pnt1.X)**2
			+(pnt2.Y-pnt1.Y)**2
			+(pnt2.Z-pnt1.Z)**2)**0.5)

# The input list of points .
points = IN[0]


farthestDistance=distance(points[0],points[1])

# The output list of distances .
farthestPoints=[]

for i in range(len(points)):
	for j in range(len(points)):
		if i == j:
			pass
		else:
			if distance(points[i],points[j])>farthestDistance:
				farthestDistance=distance(points[i],points[j])
				farthestPoints.Clear()
				farthestPoints.append(points[i])
				farthestPoints.append(points[j])

OUT=farthestPoints