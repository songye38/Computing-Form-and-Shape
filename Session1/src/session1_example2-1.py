import rhinoscriptsyntax as rs
import random
import math

z = 0
radius = 5
theta = 0

while z <=1000:
    x = radius * math.cos(theta)
    y = radius * math.cos(theta)
    rs.AddPoint((x,y,z))
    radius += .008
    theta +=.08
    z = z + .01
