import random

class Point: #name for  class, same rules for variables apply; capital letter to signal it's a class
    #innit method = what you are doing when you're initializing a class
    def __init__(self, x, y): #it's no longer a function, it's a method now since it's inside a class
        # self = parameter, convention, th
        """
        Initialize a Point object
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x #self is used to represent an instance (object) of a class
        self.y = y #define y attribute via self.y and assign the value y to it

    def __str__(self): # str needs to be indented & follow the init
        """
        magic methos that is called when we try to print an instance
        :return: <x, y>
        """
        return f"p{self.x, self.y}"

    def distance_orig(self):
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other): #need to include this other; gt = greater than
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self, other): #eq = equal
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance

# now we need to instantiate it
p = Point(1, 2) # p is an instance of 1 and 2
p2 = Point(2, 3)
p3 = Point(4.4, -55)
print(f"p.x={p.x} and p.y={p.y}")
# the {} you're replacing it with the value of p.x
print(f"p3.x={p3.x} and p3.x={p3.x}")
# you can accedd and change this info
p.x = 20
print(f"p.x={p.x} and p.y={p.y}") # printing attributes of the instance
print(p) # will give u something weird back, since it doesn't know what you want to be printed
    # after adding the str definition thing, it will now print (x, y)

print(p2)
print(p3)

# create a list of 5 random points --> import random
# imports are usually added at the start
points = []
for i in range (5):
    points.append(Point(random.randint(-10, 10), # x value
                        random.randint(-10, 10))) #y value

print("I get these 5 random points:")
for p in points:
    print(p)

# end goal: sort our list of points. To do this, we have to be able to compare two points
    # maybe by distance
print(points)

p = Point(3, 4)
print(p.distance_orig()) #expect 5 answers

p2 = Point(1, 1)
print(p > p2) # the answer should be true
print(f"I am comparing p > p2: {p > p2}")

print("the sorted list of points is:")
points.sort()
print(points)

class ColorPoint(Point):



colors = ["red", "green", "blue", "yellow", "black", "magenta",
          "cyan", "white", "burgundy", "periwinkle", "marsala"]

color_points = []
for i in range(10):
    color_points.append(
        ColorPoint(random.randint(-10, 10),
                   random.randint(-10, 10),
                   random.choice(colors))
    )