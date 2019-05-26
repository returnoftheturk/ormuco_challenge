# Your goal for this question is to write a program that accepts two lines (x1,x2)
#  and (x3,x4) on the x-axis and returns whether they overlap. 
# As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

def findOverlap(x1, x2):
    return (x2[1]<x1[1] and x2[1]>x1[0]) or (x2[0]<x1[1] and x2[0]>x1[0])

print(findOverlap((1,5),(6,9)))
print(findOverlap((-5,1),(2,9)))
print(findOverlap((-100,-50),(-200,-99)))
print(findOverlap((-100,-50),(-51,-9)))
print(findOverlap((-100,-50),(-49,1000)))