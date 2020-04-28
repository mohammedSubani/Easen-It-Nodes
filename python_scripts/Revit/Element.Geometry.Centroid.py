#First Node
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
# Get elements geometry
elem = IN[0]

OUT=elem.Geometry()[0]
#Second Node

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

geom = IN[0]
surface=IN[1]

if isinstance(geom,Solid):
	OUT=geom
else:
	OUT=surface

# centroids can be for solids or surfaces

#Last Node
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

geom = IN[0]

# finds the centroid for any of the following 
if isinstance(geom,Solid):
	OUT=Solid.Centroid(geom)
elif isinstance(geom,Surface):
	OUT=Surface.PointAtParameter(geom[0],0.5,0.5)
elif isinstance(geom,Curve):
	OUT=Curve.PointAtParameter(geom,0.5)
else:
	OUT='Bad Input Type'