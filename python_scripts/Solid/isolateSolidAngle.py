# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The input list for these nodes .
inSolid = IN[0]
angle_1=IN[1]
angle_2=IN[2]
angle_3=IN[3]

# Find solid centroid to creat a coordinate system at the normal of that plane and eventually rotating the desired angle and cut it by two planes and return the gometry within those two planes.

centroid=Solid.Centroid(inSolid)
mainPlane=Plane.ByOriginNormal(centroid,Vector.ByCoordinates(0,0,1))
plane_1=Geometry.Rotate(mainPlane,centroid,Vector.ByCoordinates(0,1,0),angle_1)
plane_2=Geometry.Rotate(mainPlane,centroid,Vector.ByCoordinates(0,1,0),angle_2)
plane_3=Geometry.Rotate(mainPlane,centroid,Vector.ByCoordinates(1,0,0),angle_3)
firstSplit=Geometry.Split(inSolid,plane_1)
secondSplit=Geometry.Split(firstSplit[0],plane_2)
lastSplit=Geometry.Split(firstSplit[0],plane_3)

OUT = lastSplit[1]