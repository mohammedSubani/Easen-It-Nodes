# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
                          

# The inputs to this node will be stored as a list in the IN variables.
crv = IN[0]
approxParameter=IN[1]
# A method that creates and approximation lines for a curvilnear
def getCurveAprox(curve,approxParameter):
	approxParameter+=1
	parameters=[]
	step=1.0/(approxParameter-1)
	for i in range(0,approxParameter):
		parameters.append(i*step)
	pntsAtParam=[]
	for i in parameters:
		pntsAtParam.append(Curve.PointAtParameter(curve,i))
	lines=[]
	for i in range(1,len(pntsAtParam)):
		lines.append(Line.ByStartPointEndPoint(pntsAtParam[i-1],pntsAtParam[i]))
	return lines

OUT =getCurveAprox(crv,approxParameter)
