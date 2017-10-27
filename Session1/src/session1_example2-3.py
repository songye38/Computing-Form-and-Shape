import rhinoscriptsyntax as rs
import random
import math

z = 0  #height
radius = 0 #radius of circle
theta = 0  #angle

while z <=300:
    x = radius * math.cos(theta)
    y = radius * math.cos(theta)
    rs.AddPoint((x,y,z))
    radius += .08
    theta +=.08
    z = z + .05


#adjust the radius
#to start from 0
#and add .08
# no limit
#adjust the total height
#height maximum to 300
