import rhinoscriptsyntax as rs
import random

myPoint = (2,5,1)

#session2 - 3 Lists and Touples in preparation for rhinoscript curve functions


#a is tuple type
#tuple can have types of number
a = (1,2,30,1000,"apple", 3453123.5432444, "yes, a string can be quite long even annoying")

#b is list
# list uses bracket
# it also has different types of data
b = [7,4,2.0, -33450, "peer", "python programming is a joy and a pleasure"]


#how can we access each data
#-> by using index
#index means spot in the data
#index counting starts at 0

print(a[1])  # it will print 2
print(b[3])  #it will print -33450

#what is the size of list b ?
print(len(b))

#list can be modified
b[3] = 0 # -33450 -> 0

#append function comes with list
b.append(40) # add 40  end of list

print(len(b))   # now we have 7 items in list b and 40 will be last number

#list and tuple can be in the list
c = [6,6,2,20,3, [4,5,-75.3,0, "pear"], (4,5,6)]
c.append(20)
print (c[5][1])
