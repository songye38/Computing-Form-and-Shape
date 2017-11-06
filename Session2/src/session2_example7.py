#session2 - 6
#nesting loops to create many curves with random values


import rhinoscriptsyntax as rs
import random

#we can establish 10 curves
for c in range(3):
    #we have to create list to append point
    listOfPoints = []
    for q in range(50):
        v1 = random.uniform(-100,100)
        v2 = random.uniform(-100,100)
        v3 = random.uniform(-100,100)
        listOfPoints.append([v1,v2,v3])
    #outside of inner for loop
    rs.AddInterpCurve(listOfPoints,3)
