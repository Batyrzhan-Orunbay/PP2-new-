#1
import math
def degree_to_radian(d):
    return d * (math.pi/180)
d=int(input("Degree: "))
print("Radian: ", degree_to_radian(d))

#2
import math
def area(a,b,h):
    return (a+b)/2 * h
h=int(input("Height: "))
a=int(input("Base, first value: "))
b=int(input("Base, second value: "))
print("Expected Output: ", area(a,b,h))

#3
from math import tan,pi
def area(s,l):
    return s * (l**2) / (4*tan(pi/s))
s=int(input("Input number of sides: "))
l=int(input("Input the length of a side: "))
print("The area of the polygon is: ", area(s,l))

#4
import math
def area(a,h):
    return a * h
a=int(input("Length of base: "))
h=int(input("Height of parallelogram: "))
print("Expected Output: ", area(a,h))