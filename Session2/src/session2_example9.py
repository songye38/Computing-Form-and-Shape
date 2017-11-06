#session2 - 7
#createing functions, curves within a volume, and flat curves


import rhinoscriptsyntax as rs
import random

def randoCurve(nPoints):
    listOfPoints = []
    for q in range(nPoints):
        v1 = q
        #v2 is y value
        v2 = random.triangular(-100,100,50)
        #v3 always be 0
        v3 = 0
        listOfPoints.append([v1,v2,v3])
    rs.AddInterpCurve(listOfPoints,3)


#example 9-1
randoCurve(10)

#example 9-2
#positive area has more curves
#because of triangular functions
#mode value is 50 so it tends to close 50
randoCurve(1000)
