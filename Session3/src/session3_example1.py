#session3 - 2
# using "GetObjects" function

import rhinoscriptsyntax as rs
import random

pickedCurves = rs.GetObjects("pick some curves", 4)

for curve in pickedCurves:
    vector = (random.uniform(-2,2), random.uniform(-2,2), random.uniform(-2,2))
    rs.CopyObject(curve,vector)
