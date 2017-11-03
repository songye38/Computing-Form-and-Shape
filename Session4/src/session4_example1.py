#session4 - 4,5
# evaluating surface using U and V coordinates

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


numberUCells = 9
numberVCells = 11


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
        pointA = rs.EvaluateSurface(srf,U,V)
        pointB = rs.EvaluateSurface(srf,U+uStep,V)
        pointC = rs.EvaluateSurface(srf,U+uStep,V+vStep)
        pointD = rs.EvaluateSurface(srf,U,V+vStep)

        #give us a poly line
        #take a list of values
        #point a-> point b -> point c-> point d -> point a to close rectangle
        #you don't have to make rectangle shape
        poly = rs.AddPolyLine([pointA,pointB,pointC,pointD,pointA])

        #would be easy to do all sorts of extra line work here based on an awraness of a,b,c,d

        V +=vStep
    U +=uStep
