# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Input list
line_1=IN[0]
line_2=IN[1]
centerPnt=IN[2]
# method that creates an arc and returns the sweeep angle for that arc
def BetweenLinesArcAngle(line_1,line_2,midPnt):
	arcStartPnt=Curve.PointAtParameter(line_1,0.5)
	arcEndPnt=Curve.PointAtParameter(line_2,0.5)
	arc=Arc.ByCenterPointStartPointEndPoint(midPnt,arcStartPnt,arcEndPnt)
	angle=Arc.SweepAngle.GetValue(arc)
	return angle
	
OUT = BetweenLinesArcAngle(line_1,line_2,centerPnt)