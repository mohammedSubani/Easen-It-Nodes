# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
solid=IN[0]
quarterNumber=IN[1]

# Create a golbal quarters to return the solid within a given quarter determined by the quarter number .
originPoint=Point.ByCoordinates(0,0,0)
cutPlane_1=Plane.ByOriginNormal(originPoint,Vector.ByCoordinates(0,0,1))
cutPlane_2=Plane.ByOriginNormal(originPoint,Vector.ByCoordinates(0,1,0))
cutPlane_3=Plane.ByOriginNormal(originPoint,Vector.ByCoordinates(1,0,0))


firstCut=Geometry.Split(solid,cutPlane_1)

result='No geometry was cut'

#Choose upper or lower half
try:
	if quarterNumber<1 or quarterNumber>8:
		raise IndexError('Invalid Quarter')
	if quarterNumber<5:
		
		#Choose right or left half
		secondCut=Geometry.Split(firstCut[0],cutPlane_2)
		if quarterNumber<3:
			thirdCut=Geometry.Split(secondCut[0],cutPlane_3)
			if quarterNumber==1:
				result=thirdCut[0]
			else:
				result=thirdCut[1]
		else:
			thirdCut=Geometry.Split(secondCut[1],cutPlane_3)
			if quarterNumber==3:
				result=thirdCut[0]
			else:
				result=thirdCut[1]
	else:	
		secondCut=Geometry.Split(firstCut[1],cutPlane_2)
		if quarterNumber<7:
			thirdCut=Geometry.Split(secondCut[0],cutPlane_3)
			if quarterNumber==5:
				result=thirdCut[0]
			else:
				result=thirdCut[1]
		else:
			thirdCut=Geometry.Split(secondCut[1],cutPlane_3)
			if quarterNumber ==7:
				result=thirdCut[0]
			else:
				result=thirdCut[1]
except IndexError as e:
	result=e

OUT = result