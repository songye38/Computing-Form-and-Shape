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
    rs.AddInterpCurve(listOfPoints,3)


def veryBlipCurve(y):
    x1 = random.uniform(0,10)
    z1 = random.uniform(0,10)

    x2 = random.uniform(10,20)
    z2 = random.uniform(10,1000) # VERY BLIP

    x3 = random.uniform(20,30)
    z3 = random.uniform(10,20)

    x4 = random.uniform(3,40)
    z4 = random.uniform(0,10)

    x5 = random.uniform(40,50)
    z5 = random.uniform(0,10)

    listOfPoints = [(x1,y,z1), (x2,y,z2), (x3,y,z3),(x4,y,z4),(x5,y,z5)]
    rs.AddInterpCurve(listOfPoints,3)

for c in range(1000):
    if c == 678:
        veryBlipCurve(c)
    else:
        blipCurve(c)
