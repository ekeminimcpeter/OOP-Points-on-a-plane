'''
Let's visit a very special place – a plane with the Cartesian coordinate system (you can learn more about this concept here: https://en.wikipedia.org/wiki/Cartesian_coordinate_system).

Each point located on the plane can be described as a pair of coordinates customarily called x and y. We want you to write a Python class which stores both coordinates as float numbers. Moreover, we want the objects of this class to evaluate the distances between any of the two points situated on the plane.

The task is rather easy if you employ the function named hypot() (available through the math module) which evaluates the length of the hypotenuse of a right triangle (more details here: https://en.wikipedia.org/wiki/Hypotenuse) and here: https://docs.python.org/3.7/library/math.html#trigonometric-functions.

This is how we imagine the class:

    it's called Point;
    its constructor accepts two arguments (x and y respectively), both of which default to zero;
    all the properties should be private;
    the class contains two parameterless methods called getx() and gety(), which return each of the two coordinates (the coordinates are stored privately, so they cannot be accessed directly from within the object);
    the class provides a method called distance_from_xy(x,y), which calculates and returns the distance between the point stored inside the object and the other point given as a pair of floats;
    the class provides a method called distance_from_point(point), which calculates the distance (like the previous method), but the other point's location is given as another Point class object;
Complete the template we've provided in the editor and run your code and check whether your output looks the same as ours.

Expected output
1.4142135623730951
1.4142135623730951

'''

#Author: Ekemini Peter [McCoy McPeter]
#Description: Original code implementation of distance between points on plane with cartesian coordinate system calculator.
#Date: 27/05/2025
#Version: Rev 0

import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x # store x cordinate 
        self.__y = y # store y cordinate 

    def getx(self):
        return self.__x # returns x cordinate 

    def gety(self):
        return self.__y # returns y cordinate

    def distance_from_xy(self, x, y):
        self.__x1 = x # store x cordinate of a relative point
        self.__y1 = y # store y cordinate of a relative point
        x_difference = self.getx() - self.__x1 # find difference in the x cordinates
        y_difference = self.gety() - self.__y1 # find difference in the y cordinates
        #self.distance_from_xy = math.hypot(x_difference,y_difference) # the .hypo() function finds the length of the hypotenus of a triangle 
        self.distance_from_xy = math.sqrt(x_difference**2 + y_difference**2) # calculates the distance between two referenced points
        return self.distance_from_xy
   
    def distance_from_point(self, point):
        self.__point = point # create private attribute for referenced point 
        self.__x_point = self.__point.getx() #read and store x cordinate 
        self.__y_point = self.__point.gety() #read and store y cordinate
        x_difference = self.getx() - self.__x_point
        y_difference = self.gety() - self.__y_point
        self.distance_from_point = math.hypot(x_difference,y_difference)
        return self.distance_from_point


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

