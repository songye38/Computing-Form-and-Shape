#session2 - 7
#createing functions, curves within a volume, and flat curves


import rhinoscriptsyntax as rs
import random

#we create our own functions
#function also uses indentation
def randoCurve(nPoints):
    listOfPoints = []
    for q in range(nPoints):
        v1 = random.uniform(-100,100)
        v2 = random.uniform(-100,100)
        v3 = random.uniform(-100,100)
        listOfPoints.append([v1,v2,v3])
    rs.AddInterpCurve(listOfPoints,3)


#example 1
#we can call randoCurve function
#randoCurve(10)
#randoCurve(1000)


#example 2

for c in range(10):
    randoCurve(c+2)
