import clr
import sys
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import random

srfc = IN[0]
pointsDensityFactor=IN[1]
points=[]


for i in range(pointsDensityFactor):
	p=Surface.PointAtParameter(srfc, random.random(), random.random())
	points.append(p)


OUT = points
