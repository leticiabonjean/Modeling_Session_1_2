from point import Point
import random
#
class PointException(Exception):
    pass #i think it won't run the code???? not sure

class ColorPoint(Point):
    """
    Subclass of Point for organizational/additional purposes. Adds a color attribute to the point.
    """
    def __init__(self, x, y, color):
        """
        Initializes an object with coordinates (x, y) and a color (color)
        :param x: x position on the axis (as a float or int)
        :param y: y position on the axis (as a float or int)
        :param color: color of the point as a string
        """
        if not isinstance(x, (int, float)):
            raise PointException("x must be a number") # checking that x is a number
        if not isinstance(y, (int, float)): # these are RESTRICTIONS
            raise PointException("y must be a number") # since for dist we find square of x, y, they need to be numbers

        super().__init__(x, y)
        self.color = color
        # self.x = x
        # self.y = y there's no need to duplicate this, we can get it from the first code


    def __str__(self):
        """
        magic method that is called when we try to print an instance
        :return: color: x, y
        """
        return f"<{self.color}: {self.x}, {self.y}>"


p = ColorPoint(1, 2, "red")
#p.color = "rojo" # this is changing "red" to "rojo" --> hacking the code
    # you shouldn't be able to edit the internal attribute of the class
print(p.distance_orig()) # gives you the distance
print(p) # gives you red: 1, 2





# colors = ["red", "green", "blue", "yellow", "black", "magenta",
#           "cyan", "white", "burgundy", "periwinkle", "marsala"]
#
# color_points = []
# for i in range(10):
#     color_points.append(
#         ColorPoint(random.randint(-10, 10),
#                    random.randint(-10, 10),
#                    random.choice(colors))
