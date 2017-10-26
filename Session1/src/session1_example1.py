import rhinoscriptsyntax as rs
import random

count = 0
while count < 90000:
    x = random.uniform(-100,100)
    y = random.uniform(-100,100)
    z = random.uniform(-100,100)
    point = (x,y,z)
    if rs.Distance(point,(30,30,30))>40 and rs.Distance(point, (50,50,50))<45:
        rs.AddPoint(point)
    count = count+1
   

