# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

scaleFactor=IN[0]

# This list of icoshedron triangles.
tringulations=[]


# Create the golden ratio rectangles of the icoshedron
a=pntsXY=Polygon.Corners(Rectangle.ByWidthLength(Plane.XY(),0.618034,1))
b=pntsXZ=Polygon.Corners(Rectangle.ByWidthLength(Plane.XZ(),0.618034,1))
c=pntsYZ=Polygon.Corners(Rectangle.ByWidthLength(Plane.YZ(),0.618034,1))


# Creating triangularion by means of the corner points of these rectangles until the icoshedron is formed

tringulations.append(Surface.ByPerimeterPoints([a[1],a[2],c[0]]))
tringulations.append(Surface.ByPerimeterPoints([a[1],a[2],c[1]]))

tringulations.append(Surface.ByPerimeterPoints([a[0],a[3],c[2]]))
tringulations.append(Surface.ByPerimeterPoints([a[0],a[3],c[3]]))

tringulations.append(Surface.ByPerimeterPoints([b[1],b[2],a[0]]))
tringulations.append(Surface.ByPerimeterPoints([b[1],b[2],a[1]]))

tringulations.append(Surface.ByPerimeterPoints([b[0],b[3],a[2]]))
tringulations.append(Surface.ByPerimeterPoints([b[0],b[3],a[3]]))

tringulations.append(Surface.ByPerimeterPoints([c[1],c[2],b[0]]))
tringulations.append(Surface.ByPerimeterPoints([c[1],c[2],b[1]]))

tringulations.append(Surface.ByPerimeterPoints([c[0],c[3],b[2]]))
tringulations.append(Surface.ByPerimeterPoints([c[0],c[3],b[3]]))


tringulations.append(Surface.ByPerimeterPoints([a[0],b[1],c[2]]))
tringulations.append(Surface.ByPerimeterPoints([a[0],b[2],c[3]]))

tringulations.append(Surface.ByPerimeterPoints([a[1],b[1],c[1]]))
tringulations.append(Surface.ByPerimeterPoints([a[1],b[2],c[0]]))

tringulations.append(Surface.ByPerimeterPoints([a[2],b[0],c[1]]))
tringulations.append(Surface.ByPerimeterPoints([a[2],b[3],c[0]]))

tringulations.append(Surface.ByPerimeterPoints([a[3],b[0],c[2]]))
tringulations.append(Surface.ByPerimeterPoints([a[3],b[3],c[3]]))


# Scale the geometry of icoshedron
scaledGeom=[]

for i in tringulations:
	scaledGeom.append(Geometry.Scale(i,scaleFactor,scaleFactor,scaleFactor))
# Find each face normal plane 
normals=[]	
for i in scaledGeom:
	normals.append(Surface.NormalAtParameter(i,0.5))
# Return each face polygon
triPolygons=[]
for i in scaledGeom:
	tmp=Surface.PerimeterCurves(i)
	pnts=[]
	for j in tmp:
		pnts.append(Curve.PointAtParameter(j,0))
	triPolygons.append(Polygon.ByPoints(pnts))

# The output list for the icoshedron 
OUT = scaledGeom,triPolygons,normals