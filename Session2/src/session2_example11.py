#session2 - 8
#two "blip" strategies


import rhinoscriptsyntax as rs
import random

def blipCurve(y):
    x1 = random.uniform(0,10)
    z1 = random.uniform(0,10)

    x2 = random.uniform(10,20)
    z2 = random.uniform(10,100) # this is on purpose this is blip

    x3 = random.uniform(20,30)
    z3 = random.uniform(10,20)

    x4 = random.uniform(3,40)
    z4 = random.uniform(0,10)

    x5 = random.uniform(40,50)
    z5 = random.uniform(0,10)

    listOfPoints = [(x1,y,z1), (x2,y,z2), (x3,y,z3),(x4,y,z4),(x5,y,z5)]
    return rs.AddInterpCurve(listOfPoints,3)


whereIsBlip = random.randint(0,999)
for c in range(1000):
    aCurve = blipCurve(c)
    if c == whereIsBlip:
        rs.MoveObject(aCurve, (0,0,random.uniform(-100,-50)))
