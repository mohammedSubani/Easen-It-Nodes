# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
cl= IN[0]
volStop=IN[1]
forceComputation=IN[2]

# Creates the first cube length.
cs=Cuboid.ByLengths(cl,cl,cl)

# The output to this node will be stored as a list in this list.
result=[]

# A recursive method that will be used to define the mengerSponge geometry .
def mengerIteration(cubeSolid):
	# Find the given cube length.
	edges=Solid.Edges.GetValue(cubeSolid)
	edgeCurve=Edge.CurveGeometry.GetValue(edges[0])
	cubeLength=Curve.Length.GetValue(edgeCurve)


	# The sub-cubes to be removed to form an iteration of mengerSponge.
	popElements=(4,10,12,13,14,16,22)

	# Find the cube faces.
	cubeFaces=Topology.Faces.GetValue(cubeSolid)
	cubeSurfces=[]
	for i in cubeFaces: 
		cubeSurfces.append(Face.SurfaceGeometry(i))

	# Create first split patch by starting with the top surface.
	topSurface=cubeSurfces[0]
	# Create cutting planes.
	cuttingPlaneOrigin_firstCut=Surface.PointAtParameter(topSurface,1.0/3.0,0)
	planeNormalVector_firstCut=Surface.TangentAtUParameter(topSurface,1.0/3.0,0)
	cuttingPlane_firstCut=Plane.ByOriginNormal(cuttingPlaneOrigin_firstCut,planeNormalVector_firstCut)
	# Split the cubes.
	firstSplit=Geometry.Split(cubeSolid,cuttingPlane_firstCut)
	# The first cut patch.
	firstPatch=[]

	firstPatch.append(firstSplit[1])
	firstPatch.append(Geometry.Translate(firstSplit[1],planeNormalVector_firstCut,(1.0/3.0)*cubeLength))
	firstPatch.append(Geometry.Translate(firstSplit[1],planeNormalVector_firstCut,(1.0/3.0)*cubeLength*2))

	# Create second split patch by starting with the side surface.	
	sideSurface=cubeSurfces[2]
	# Create cutting planes.
	cuttingPlaneOrigin_secondCut=Surface.PointAtParameter(sideSurface,1.0/3.0,0)
	planeNormalVector_secondCut=Surface.TangentAtUParameter(sideSurface,1.0/3.0,0)
	cuttingPlane_secondCut=Plane.ByOriginNormal(cuttingPlaneOrigin_secondCut,planeNormalVector_secondCut)
	# Split the first patch.
	secondPatch=[]

	for i in firstPatch:
		split=Geometry.Split(i,cuttingPlane_secondCut)
		secondPatch.append(split[1])
		secondPatch.append(Geometry.Translate(split[1],planeNormalVector_secondCut,(1.0/3.0)*cubeLength))
		secondPatch.append(Geometry.Translate(split[1],planeNormalVector_secondCut,(1.0/3.0)*cubeLength*2))

	# Create the last split patch by starting with the adjacent side surface.	
	thirdSurface=cubeSurfces[3]
	# Create cutting planes.
	cuttingPlaneOrigin_thirdCut=Surface.PointAtParameter(thirdSurface,0,1.0/3.0)
	planeNormalVector_thirdCut=Surface.TangentAtVParameter(thirdSurface,0,1.0/3.0)
	cuttingPlane_thirdCut=Plane.ByOriginNormal(cuttingPlaneOrigin_thirdCut,planeNormalVector_thirdCut)
	# Split the second patch.
	lastPatch=[]
	
	for i in secondPatch:
		split=Geometry.Split(i,cuttingPlane_thirdCut)
		lastPatch.append(split[1])
		lastPatch.append(Geometry.Translate(split[1],planeNormalVector_thirdCut,(1.0/3.0)*cubeLength))
		lastPatch.append(Geometry.Translate(split[1],planeNormalVector_thirdCut,(1.0/3.0)*cubeLength*2))


	# mengerIteration cubes add everything but the popElements.
	mengerIterationCubes=[]
	
	for i in range(len(lastPatch)):
		if popElements.Contains(i):
			pass
		else:
			mengerIterationCubes.append(lastPatch[i])

	# Base Case.			
	if Solid.Volume.GetValue(mengerIterationCubes[0])<=volStop:
		result.append(mengerIterationCubes)
	else:
		for i in mengerIterationCubes:
			mengerIteration(i)
			

# Calling the method.	
if float(cl)/volStop > 0.2923976608187 and forceComputation == False:
	result.append('High computation cost try to make cubeLength to stopVolume ratio less than 0.29239')
else:
	mengerIteration(cs)
    
OUT = result


