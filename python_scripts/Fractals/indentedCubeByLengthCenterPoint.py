# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
length = IN[0]
stoppingLength=IN[1]
centerPoint=IN[2]
# The output to this node will be stored as a list in this list.
result=[]


def recursiveCubes(length):
	#Create a the cube.
	cube=Cuboid.ByLengths(centerPoint,length,length,length)
	facesOfCube=Topology.Faces.GetValue(cube)

	# UV coordinates to form a rectangle of solid-cut extrusion.
	UVCoordinate=((0.1,0.1),(0.1,0.9),(0.9,0.9),(0.9,0.1))

	# Define three surfaces to the cube to from the cutting solids.
	srfc1=Face.SurfaceGeometry(facesOfCube[0])
	srfc2=Face.SurfaceGeometry(facesOfCube[2])
	srfc3=Face.SurfaceGeometry(facesOfCube[5])

	# Define points for the cutting entities.
	firstPatch=[]
	for i in UVCoordinate:
		firstPatch.append(Surface.PointAtParameter(srfc1,i[0],i[1]))
	secondPatch=[]
	for i in UVCoordinate:
		secondPatch.append(Surface.PointAtParameter(srfc2,i[0],i[1]))
	thirdPatch=[]
	for i in UVCoordinate:
		thirdPatch.append(Surface.PointAtParameter(srfc3,i[0],i[1]))

	# Define polygon patches of extrusion.	
	subpoly1=Polygon.ByPoints(firstPatch)
	subpoly2=Polygon.ByPoints(secondPatch)
	subpoly3=Polygon.ByPoints(thirdPatch)

	# Extrusion of solid-cut cubes.
	subCubes=[]
	subCubes.append(Curve.ExtrudeAsSolid(subpoly1,Vector.ByCoordinates(0,0,-1),length*2))
	subCubes.append(Curve.ExtrudeAsSolid(subpoly2,Vector.ByCoordinates(0,1,0),length*2))
	subCubes.append(Curve.ExtrudeAsSolid(subpoly3,Vector.ByCoordinates(-1,0,0),length*2))
	# Base case to stop the recursion.
	if length*0.9<stoppingLength:
		result.append(Cuboid.ByLengths(centerPoint,length*0.9,length*0.9,length*0.9))
		return
	# Apply subtraction.
	result.append(Solid.DifferenceAll(cube,subCubes))
	recursiveCubes(length*0.9)


# Calling the recursive method.
recursiveCubes(length)

OUT=result  