# Enable Python support and load DesignScript library
import clr
import sys
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import random
import math

# The inputs to this node will be stored as a list in the IN variables.
startLine = IN[0]
length=IN[1]
numberOfBranches=IN[2]
stopLevel=IN[3]
alphaAngle=IN[4]

# The output to this node will be stored as a list in this list.
resultTreeLines=[]

# A recursive method to create the tree structure.
def createTree(baseLine,level=0):
	# Base Case .
	if level == stopLevel:
		return
	# Temporary list to store the current iteration lines.
	tmp=[]
	# Defining the branches start at the end of the baseLine.
	endPnt=Curve.EndPoint.GetValue(baseLine)
	endPntTangent=Curve.TangentAtParameter(baseLine,1)
	jointPlane=Plane.ByOriginNormal(endPnt,endPntTangent)
	cs=CoordinateSystem.ByPlane(jointPlane)
	thetaAngle=360.0/numberOfBranches
	# Creating the iteration branches.
	for i in range(numberOfBranches):
		directionPnt=Point.BySphericalCoordinates(cs,alphaAngle,i*thetaAngle,length)
		direction=Vector.ByTwoPoints(endPnt,directionPnt)
		newLine=Line.ByStartPointDirectionLength(endPnt,direction,length)
		tmp.append(newLine)
	# Adding iteration lines to resultTreeLines list.
	resultTreeLines.append(tmp)
	# Calling itself
	for i in tmp:
		createTree(i,level+1)
		
# First Call .
createTree(startLine)
	
OUT = resultTreeLines
