import rhinoscriptsyntax as rs
import random

random.seed(2)
myVal = random.uniform(1,10)
print(myVal)

random.seed(1)
myVal = random.uniform(1,10)
print(myVal)
