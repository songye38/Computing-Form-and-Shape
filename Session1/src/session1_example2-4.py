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
    theta +=.9
    z = z + .05


#adjust the theta
#so the math.cos function add more wide angle
#space between the point is larger than before
#adjust the total height
#height maximum to 300
