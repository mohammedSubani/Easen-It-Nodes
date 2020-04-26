# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
sidesNum = IN[0]
angle=IN[1]
stopLevel=IN[2]
scaleFactor=IN[3]
# The output to this node will be stored as a list in these variables eventually will be stored in OUT.
resultGeometry=[]


#Creating the first tulip structure polygon to be passed to fractalFrame method.
#############################################################################
c1=Circle.ByCenterPointRadius(Point.ByCoordinates(0,0,0),1)
c2=Circle.ByCenterPointRadius(Point.ByCoordinates(0,0,0),0.9)
#############################################################################
p1=Polygon.RegularPolygon(c1,sidesNum)
p2=Polygon.RegularPolygon(c2,sidesNum)
#############################################################################
s1=Surface.ByPatch(p1)
s2=Surface.ByPatch(p2)
#############################################################################
sol1=Surface.Thicken(s1,0.1)
sol2=Surface.Thicken(s2,0.1)
#############################################################################
frameSolid=Solid.Difference(sol1,sol2)



#This method scales and returns a tanslated vertically version of the first frame and stops at the given level.
def fractalFrame(solid,level=0):
	if level > stopLevel:
		return
	translation=Geometry.Translate(solid,0,0,-0.1)
	plane=Plane.ByOriginNormal(Point.ByCoordinates(0,0,0),Vector.ByCoordinates(0,0,1))
	rotation=Geometry.Rotate(translation,plane,angle)
	scale=Geometry.Scale(rotation,scaleFactor,scaleFactor,scaleFactor)
	resultGeometry.append(scale)
	fractalFrame(scale,level+1)
	

#Calling the method with the first frame.

fractalFrame(frameSolid)


OUT = resultGeometry


                          