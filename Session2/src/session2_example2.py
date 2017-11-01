import rhinoscriptsyntax as rs
import random

# use three random functions

#seed makes the result same
random.seed(1)
myVal = random.uniform(1,10)
print(myVal)

myVal = random.randint(1,10)
print(myVal)

#middle between the two values 2 gives cluser of value 2 if we run this program over and over
myVal = random.triangular(1,10,2)
print(myVal)
