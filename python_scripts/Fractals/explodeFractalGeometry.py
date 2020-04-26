# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
fractalGeometry = IN[0]

# List of outputs if nothing is stored in the list it means Geometry doesn't consist of that type.
surfaces=[]
curves=[]
points=[]


if isinstance(fractalGeometry[0],Solid):
# Test for solids.
	for i in fractalGeometry:
		faces=Solid.Faces.GetValue(i)
		tmp=[]
		for j in faces:
			tmp.append(Face.SurfaceGeometry(j))
		surfaces.append(tmp)
if isinstance(fractalGeometry[0],Surface):
# Test for surfaces.
	for i in fractalGeometry:
		crvs=Surface.PerimeterCurves(i)
		curves.append(crvs)
if isinstance(fractalGeometry[0],Curve):
# Test for curves.
	for i in fractalGeometry:
		pnts=[]
		pnts.append(Curve.PointAtParameter(i,0.5))
		pnts.append(Curve.PointAtParameter(i,0.0))
		pnts.append(Curve.PointAtParameter(i,1.0))
		points.append(pnts)
OUT = surfaces,curves,points

