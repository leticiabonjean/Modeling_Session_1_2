from color_point import ColorPoint, PointException

class AdvancedPoint(ColorPoint):
    """
    Subclass of Colorpoint with additional validation, properties, and methods.
    """
    COLORS = ["red", "blue", "periwinkle", "orange", "green", "pink", "purple", "black", "white"] # this is the class attribute
        # every point should have a color
    def __init__(self, x, y, color):
        """
        Initializes an AdvancedPoint object. validates that the color in the allowed COLORS list.
        :param x: x position on the axis
        :param y: y position on the axis
        :param color: color of the point (from COLORS list)
        """
        if color not in self.COLORS:
            raise PointException(f"Invalid color: must be one of {self.COLORS}") #checking the colors
        self._x = x
        self._y = y
        self._color = color
#
    @property #shortcut to make life easier; it's like a type of method
    def x(self):
        """
        Getter method for the x-coordinate.
        :return: x-coordinate
        """
        return self._x #getter method

    @x.setter
    def x(self, value): #add the value tha you want to set it as, if you want to change it in the future
        """
        Setter method for the x-coordinate.
        :param value: New x-coordinate value
        """
        self._x = value #setter method
        #it's basically you establishing what you'd like an attribute to be based on some info that you will give

    @property
    def y(self):
        """
        Getter method for the y-coordinate.
        :return: y-coordinate
        """
        return self._y

    @property
    def color(self):
        """
        Getter method for the color.
        :return: color of the point
        """
        return self._color

    @classmethod #classmethod = something that changed the class, like adding a new color
        #applies to the class as a whole. for when you're changing something about the class itself, not the instance
    def add_color(cls, color): #cls = short for class
        """
        dds a new color for our class
        :param color: new color tobe added
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color = "red"): #create a new point from a tuple, x & y as individual tuples
        """
        Creates a new point from a tuple, rather than 2 individual values
        :param coordinate: tuple containing (x,y)
        :param color: optional color
        :return: new AdvancedPoint instance (x, y, color)
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Static method to calculate the distance between teo point-like objects
        :param p1: first point-like object with x and y attributes
        :param p2: second point-like object with x and y attributes
        :return: Distance between p1 and p2
        """
        return((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        """
        Instance method to calculate the distance from self (AdvancedPoint instance) to another point-like object
        :param p: another point-like object with x and y attributes
        :return: distance between self and p
        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5 # same as the static method above

AdvancedPoint.add_color("rojo") #METHOD
    #pass   #--> when you are forced to have a code by syntax, but you don't want any code
           # it would just rename the class as "AdvancedPoint"

p = AdvancedPoint(1, 2, "red")
print(p)
print(p.distance_orig())
p2 = AdvancedPoint.from_tuple((3, 2)) #putting them in a tuple, and calling the method
    # the "red" comes from the definition
print(p2)

print(AdvancedPoint.distance_2_points(p, p2)) # takes (1,2) and (3,2) ^^^
print(p.distance_to_other(p2)) # here you're including the other point, "p", in the beginning
    # gives you the same result as the static method way
    # for the static method, instead of self, it's another point
