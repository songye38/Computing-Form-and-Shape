#session4 - 6
# curves at surface normal, aka porcupine surface

import rhinoscriptsyntax as rs
import random


#picking object using GetObjects functions
#in this case we'll use GetObject because we want to deal with only 1 object
#we'are not gonna looping through multiple surfaces
#GetObject function tells users to pick only 1 surface
# filter value 8 means surface
srf = rs.GetObject("pick some surface",8)

#if we deal with only 1 object
#we can use object identifier instead
#in command line type what and rhino will tell us object's identifier
#but this is somewhat ineffient when we have to pick up different object
#srf="we can copy the object id to here"


numberUCells = 20
numberVCells = 60


#tells us the extence of surface
#where does the U starts and V starts
#0 is for U
#1 is for V
#domain will be tuple it has low value and high value
uDomain = rs.SurfaceDomain(srf,0)
vDomain = rs.SurfaceDomain(srf,1)

#you can print uDomain and vDomain to see the value
#but this part is just for demonstration
# print (uDomain)
# print (vDomain)

#pointCoordinates is just coordinates
# pointCoordinates1 = rs.EvaluateSurface(srf,10,10)

# #by using Addpoint function we can make pointCoordinates into point object
# rs.AddPoint(pointCoordinates)


uMin = uDomain[0]
uMax = uDomain[1]
vMin = uDomain[0]
vMax = uDomain[1]


#find the range of the surface by subtracint the max value and min value
#what is the width and length of the surface
uRange = uMax - uMin
vRange = vMax - vMin

uStep = uRange / numberUCells
vStep = vRange / numberVCells

U = uMin

#we start at U and looping through all V
#and then next U and looping thought all V
#when this is done we establish a grid
while U < uMax:
    V = vDomain
    while V< vMax:

        #SurfaceNormal function takes U and V as one tuple
        #in this function you have to take them in the paranthesis
        normal = rs.SurfaceNormal(srf,(U,V))
        scaledNormal = rs.VectorScale(normal,10)

        #pointOnSurface is base surface
        pointOnSurface = rs.EvaluateSurface(srf,U,V)

        #pointOffSurface is result of add vector to the base
        pointOffSurface = rs.VectorAdd(pointOnSurface,scaledNormal)
        rs.AddLine(pointOnSurface,pointOffSurface)
        V +=vStep
    U +=uStep
