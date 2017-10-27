import rhinoscriptsyntax as rs
import random
import math

z = -100  #height start from -100 to 100
radius = 5
theta = 0

count =0
while z <=100:
    #for once this is called in this if statement radius is bigger 
    if count %2 ==0:
        x = (radius+5) * math.cos(theta)
        y = (radius+5) * math.sin(theta)
    #and next time this loop is called it reverse automatically
    else:
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

    rs.AddPoint((x,y,z))
    radius += .003
    theta += 1
    z += .01
    count+=1
