# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
inCube=IN[0]
stopRecursionVol=IN[1]

# The output to this node will be stored as a list in this list.
outCubes=[]

# A method for the recursive cubes.
def recursiveCube(cube):
	# Base Case.
	if Cuboid.Volume.GetValue(cube)<stopRecursionVol:
		return
	# Get cube faces surfaces.
	faces=Topology.Faces.GetValue(cube)
	srfcs=[]
	for i in faces:
		srfcs.append(Face.SurfaceGeometry(i))
	# Create sub-cubes on each surface.
	newPnts=[]
	for i in srfcs:
		newPnts.append(Surface.PointAtParameter(i,0.5,0.5))
	newWidth=Cuboid.Width.GetValue(cube)*0.61803398875
	newLength=Cuboid.Length.GetValue(cube)*0.61803398875
	newHeight=Cuboid.Height.GetValue(cube)*0.61803398875
	tmpCubes=[]
	for i in newPnts:
		tmpCubes.append(Cuboid.ByLengths(i, newWidth, newLength, newHeight))		
		outCubes.append(Cuboid.ByLengths(i, newWidth, newLength, newHeight))
	# Calling itself.
	for i in tmpCubes:
		recursiveCube(i)
		
		
# First Call		
recursiveCube(inCube)

OUT = outCubes

