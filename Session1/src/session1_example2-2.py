import rhinoscriptsyntax as rs
import random
import math

z = 0  #height
radius = 5 #radius of circle
theta = 0  #angle

while z <=1000:
    x = radius * math.cos(theta)
    y = radius * math.cos(theta)
    rs.AddPoint((x,y,z))
    radius += .008
    theta +=.08
    z = z + .05
