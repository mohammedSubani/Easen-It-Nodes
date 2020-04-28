import clr
import sys
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import random

element= IN[0]
closedCurve=element.Geometry()

surface = Surface.ByPatch(closedCurve[0])
pointsDensityFactor=IN[1]
points=[]
withinSurfacePoints=[]

def isWithinSurface(pnt,srfc):
	firstVertex=Surface.PointAtParameter(srfc,0,1)
	secondVertex=Surface.PointAtParameter(srfc,1,0)
	thirdVertex=Surface.PointAtParameter(srfc,0,0)
	fourthVertex=Surface.PointAtParameter(srfc,1,1)
	
	line_1=Line.ByStartPointEndPoint(pnt,firstVertex)
	line_2=Line.ByStartPointEndPoint(pnt,secondVertex)
	line_3=Line.ByStartPointEndPoint(pnt,thirdVertex)
	line_4=Line.ByStartPointEndPoint(pnt,fourthVertex)
	
	firstCond=Geometry.DoesIntersect(line_1,srfc)
	secondCond=Geometry.DoesIntersect(line_2,srfc)
	thirdCond=Geometry.DoesIntersect(line_3,srfc)
	fourthCond=Geometry.DoesIntersect(line_4,srfc)
	
	if firstCond and secondCond and thirdCond and fourthCond:
		return True
	else:
		return False

for i in range(pointsDensityFactor):
	points.append(Surface.PointAtParameter(surface, random.random(), random.random()))

for i in points:
	if isWithinSurface(i,surface):
		withinSurfacePoints.append(i)

		
OUT = withinSurfacePoints,surface