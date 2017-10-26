import rhinoscriptsyntax as rs
import random
import math

z = -100
radius = 5
theta = 0

while z <=100:
    x = radius * math.cos(theta)
    y = radius * math.sin(theta)
    rs.AddPoint((x,y,z))
    radius += .008
    theta +=.5
    z = z + .01

