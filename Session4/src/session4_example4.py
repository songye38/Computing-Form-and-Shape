#session4 - 8
# roaming lines, random paths along a surface

import rhinoscriptsyntax as rs
import random
import math

srf = rs.GetObject('pick surface',8)

uDomain = rs.SurfaceDomain(srf,0)
vDomain = rs.SurfaceDomain(srf,1)

uMin = uDomain[0]
uMax = uDomain[1]
vMin = vDomain[0]
vMax = vDomain[1]

u = random.uniform(uMin,uMax)
v = random.uniform(vMin,vMax)


for step in range(100):
    previousU = u
    previousV = v
    u += random.uniform(-1,1)
    v += random.uniform(-1,1)

    pointOnSurfaceStart = rs.EvaluateSurface(srf,previousU,previousV)
    pointOffSurfaceEnd = rs.EvaluateSurface(srf,u,v)

    rs.AddLine(pointOnSurfaceStart,pointOffSurfaceEnd)
