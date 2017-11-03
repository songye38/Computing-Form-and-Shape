#session4 - 7
# recursive algorithms and the design of a tree function

import rhinoscriptsyntax as rs
import random

#this function has default value in this case we don't have to give third value
def tree(trunk, desiredLevel, currentLevel=0):
    endPoint = rs.CurveEndPoint(trunk)

    #endPoint[0] is x endPoint[1] is y endPoint[2] is z value
    #only endPoint[2] is 0 to 5 to make tree grow vertically
    newPoint1 = (endPoint[0]+random.uniform(-5,5),endPoint[1]+random.uniform(-5,5),endPoint[2]+random.uniform(0,5))
    newPoint2 = (endPoint[0]+random.uniform(-5,5),endPoint[1]+random.uniform(-5,5),endPoint[2]+random.uniform(0,5))

    #endPoint became the starting point here
    newBranch1 = rs.AddLine(endPoint,newPoint1)
    newBranch2 = rs.AddLine(endPoint,newPoint2)

    #this is the recursing part
    if currentLevel <desiredLevel:

        #we are creating brach of tree
        #in here we are setting the currentLevel by adding 1
        #if we do not set the currrentLevel we will be in the infinite loop
        tree(newBranch1,desiredLevel,currentLevel+1)
        tree(newBranch2, desiredLevel,currentLevel+1)


#we are creating a base line
startLine = rs.AddLine((0,0,0),(0,0,20))

#desiredlevel 3
tree(startLine,3)
