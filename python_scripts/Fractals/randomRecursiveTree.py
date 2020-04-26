# Enable Python support and load DesignScript library.
import clr
import sys
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import random

# The inputs to this node will be stored as a list in the IN variables.

startLine = IN[0]
randomLengthRange=IN[1]
numberOfBranches=IN[2]
stopLevel=IN[3]

# The output to this node will be stored as a list in this list.

resultTreeLines=[]

# A method to be used recurisvely to create a tree structure.

def createRandomTree(baseLine,level=0):
	# Base Case.
	if level == stopLevel:
		return
	# temporary list to hold current iteration lines.
	tmp=[]
	# Create a direction of the new lines at the end of the baseLine.
	endPnt=Curve.EndPoint.GetValue(baseLine)
	endPntTangent=Curve.TangentAtParameter(baseLine,1)
	jointPlane=Plane.ByOriginNormal(endPnt,endPntTangent)
	cs=CoordinateSystem.ByPlane(jointPlane)
	# Creating the branches lines.
	for i in range(numberOfBranches):
		directionPnt=Point.ByCartesianCoordinates(cs,random.random()*2-1,random.random()*2-1,random.random()+0.1)
		direction=Vector.ByTwoPoints(endPnt,directionPnt)
		newLine=Line.ByStartPointDirectionLength(endPnt,direction,random.random()*randomLengthRange+0.1)
		tmp.append(newLine)
	# Adding the tmp list to the results.
	resultTreeLines.append(tmp)
	# Calling the method again.
	for i in tmp:
		createRandomTree(i,level+1)
		
# First call for the method.		
createRandomTree(startLine)
	
OUT = resultTreeLines

