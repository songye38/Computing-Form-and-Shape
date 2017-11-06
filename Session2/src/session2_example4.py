#session2 - 4 using a "for" loop to step though lists, elements by elements


import rhinoscriptsyntax as rs
import random


#example 1
c = 0
while c <100:
    print(c)
    c += 1

# range function builds list for us

#example 2
c = range(100)
print(c)

#example 3
#start, stop, increment
#start at 5, increment by 20 until less than 300
d = range(5,300,20)

# d has to be list types
for item in d:
    print item

#example 4
for item in range(100):
    print item


#example 1 and 4 result are exactly same
