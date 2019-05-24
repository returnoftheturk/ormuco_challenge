# Your goal for this question is to write a program that accepts two lines (x1,x2)
#  and (x3,x4) on the x-axis and returns whether they overlap. 
# As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

def findOverlap(x1, x2):
    return (x2[1]<x1[1] and x2[1]>x1[0]) or (x2[0]<x1[1] and x2[0]>x1[0])

x1 = (1,5)
x2 = (6,9)
print(findOverlap(x1, x2))