import clr
import sys
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import threading
import time

start_time = time.time()

numberOfCPUs=IN[0]
surfaces=IN[1]
thickness=IN[2]
both_sides=IN[3]

class thickenSurfaces(threading.Thread):
	def __init__(self,inputList):
		self.inputList=inputList
		self.result=[]
	
	def run(self):
		for i in self.inputList:
			self.result.append(Surface.Thicken(i,thickness,both_sides))

def divideSubElements(inList):
	numbOfSubElements=int(len(inList)/numberOfCPUs)

	dividedElements=[]

	for i in range(numberOfCPUs):
		if i == numberOfCPUs-1:
			dividedElements.append(inList[i*numbOfSubElements:len(surfaces)])
		else:
			dividedElements.append(inList[i*numbOfSubElements:i*numbOfSubElements+numbOfSubElements])
	
	return dividedElements

def createThreadObjects(inList):
	threadObjects=[]
	for i in inList:
		threadObjects.append(thickenSurfaces(i))
	return threadObjects
	
divided=divideSubElements(surfaces)
threadObjs=createThreadObjects(divided)

for i in threadObjs:
	i.run()

results=[]

for i in threadObjs:
	results.append(i.result)
	
elapsedTime=time.time()-start_time

elapsedTimeStr='Done in ' + repr(elapsedTime) + ' Seconds'
OUT=results,elapsedTimeStr
