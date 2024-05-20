#
#  Example program for Targil 1
# Edited by avi parshan
#
import math
from myboolfuncs import *
#
# Area calculation program  

# 2d shapes - area

def rectangleArea(w, h):
     return w*h
#
def circleArea(r):
     return math.pi * r**2

# s^2
def squareArea(s):
     return s**2

# triangle
def triangleArea(b, h):
     return (1/2) * b * h

#3d shapes - volume
def sphereVolume(r):
     return (4/3 * math.pi) * r**3

#its cone 
def coneVolume(r, h):
     return (1/3 * math.pi) * r**2 * h

#area of base (assume square) and height
def pyramidVolume(aB, h):
     # Right square pyramid
     return (1/3 * aB) * h

#cube w/ equal sides
def cubeVolume(s):
     return s**3

# printing the menu options
def prtMenu(shapes):
   for i in range(len(shapes)):
      print (i+1, shapes[i])
   return
#
# main program
#
print ("Welcome to the Area calculation program")
print ("---------------------------------------\n")  
# Print out the menu
shapes = ("Rectangle", "Circle", "Sphere", "Cone", "Square", "Square Pyramid", "Triangle", "Cube")
while True:
    print ("\nPlease select a shape (press 0 to quit):")
    prtMenu(shapes) 
    # Get the user's choice: 
    shape = input("> ")
    # Calculate the area: 
    if shape == "1":
         height = getNumber("Please enter the height: ")    
         width  = getNumber("Please enter the width: ")
         area = rectangleArea(width, height)
         print ("The area is", area)
         continue
    elif shape == "2":
         radius = getNumber("Please enter the radius: ")
         area   = circleArea(radius)
         print ("The area is", area)
         continue
    elif shape == "3":
          radius = getNumber("Please enter the radius: ")
          volume = sphereVolume(radius)
          print ("The volume is", volume)
          continue
    elif shape == "4":
          radius = getNumber("Please enter the radius: ")
          height = getNumber("Please enter the height: ") 
          volume = coneVolume(radius, height)
          print ("The volume is", volume)
          continue
    elif shape == "5":
          side = getNumber("Please enter the side: ")
          area = squareArea(side)
          print ("The area is", area)
          continue
    elif shape == "6":
          # square pyramid - base is square
          base = getNumber("Please enter the area of the base: ")
          height = getNumber("Please enter the height: ")
          volume = pyramidVolume(base, height)
          print ("The volume is", volume)
          continue
    elif shape == "7":
          # triangle
          base = getNumber("Please enter the base: ")
          height = getNumber("Please enter the height: ")
          area = triangleArea(base, height)
          print ("The area is", area)
          continue
    elif shape == "8":
         #cube - acharon acharon chaviv
          side = getNumber("Please enter the side: ")
          volume = cubeVolume(side)
          print ("The volume is", volume)
          continue
    elif shape == "0":
         print ("Bye!")
         break
    else:     
         print ("Invalid shape")
