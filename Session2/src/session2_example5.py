#session2 - 5
#creating simple curve object with random value using "addInterpCurve" function


import rhinoscriptsyntax as rs
import random

#9 random values

v1 = random.uniform(-100,100)
v2 = random.uniform(-100,100)
v3 = random.uniform(-100,100)
v4 = random.uniform(-100,100)
v5 = random.uniform(-100,100)
v6 = random.uniform(-100,100)
v7 = random.uniform(-100,100)
v8 = random.uniform(-100,100)
v9 = random.uniform(-100,100)

# 9 random value to cluser 3 point
myPointA = [v1,v2,v3]
myPointB = [v4,v5,v6]
myPointC = [v7,v8,v9]

#it take 3 point and take 3 degree
rs.AddInterpCurve([myPointA, myPointB,myPointC],3)
