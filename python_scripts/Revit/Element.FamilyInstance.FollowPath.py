import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

inputElements = IN[0]
spacing =IN[1]
facingOrientation=IN[2]
curves=[]
pCrv=[]

try:
	for i in inputElements:
		curves.append(i.Geometry()[0])
	pCrv.append(PolyCurve.ByJoinedCurves(curves))
except TypeError as e:
	pCrv.append(e)
except IndexError as e:
	pCrv.append(e)

parameterDivde=round(Curve.Length.GetValue(pCrv[0])/spacing,0)

parameters=[]

for i in range(int(parameterDivde)):
	parameters.append(i*1.0/(parameterDivde-1))
	
vectors=[]
pnts=[]

for i in range(len(parameters)):
	vectors.append(Curve.TangentAtParameter(pCrv[0],parameters[i]))
	pnts.append(Curve.PointAtParameter(pCrv[0],parameters[i]))

rotations=[]
for i in vectors:
	rotations.append(Vector.AngleWithVector(i,facingOrientation))
	

OUT = pnts,rotations
