# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
crvs = IN[0]
polyCrvs=[]

# A method to create polyCurve by certian index.
def makePolycurve(startIndex,EndIndex):
	tempCrv=[]
	for i in range(startIndex,EndIndex):
		tempCrv.append(crvs[i])
	polyCrvs.append(PolyCurve.ByJoinedCurves(tempCrv, 0.001))

firstIndex=0
for i in range(1,len(crvs)):
	if Geometry.DistanceTo(crvs[i-1],crvs[i]) != 0:
		makePolycurve(firstIndex,i-1)
		firstIndex=i
makePolycurve(firstIndex,len(crvs))

OUT=polyCrvs