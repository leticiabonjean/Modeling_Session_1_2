from color_point import ColorPoint, PointException

class AdvancedPoint(ColorPoint):
    COLORS = ["red", "blue", "periwinkle", "orange", "green", "pink", "purple", "black", "white"] # this is the class attribute
        # every point should have a color
    def __init__(self, x, y, color):
        if color not in self.COLORS:
            raise PointException(f"Invalid color: must be one of {self.COLORS}") #checking the colors
        self._x = x
        self._y = y
        self._color = color
    @property #shortcut to make life easier; it's like a type of method
    def x(self):
        """
        getter method for x-coordinate
        :return: x-coordinate
        """
        return self._x #getter method

    @x.setter
    def x(self, value):
        """
        setter for the x-coordinate
        :param value: new x-coordinate
        :return:
        """
        self._x = value #setter method

    @property
    def y(self):
        """
        getter method for y-coordinate
        :param self:
        :return:
        """
        return self._y

    @property
    def color(self):
        """
        getter fot the color of the point
        :return: color of the point
        """
        return self._color

    @classmethod #classmethod = something that changed the class, like adding a new color
        #applies to the class as a whole. for when you're changing something about the class itself, not the instance
    def add_color(cls, color): #cls = short for class
        """
        adds a new allowed color to the COLORS list
        :param color: new color to add
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color = "red"): #create a new point from a tuple, x & y as individual tuples
        """
        Creates a new point from a tuple, rather than 2 individual values
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        computed distance between two points (p1 and p2)
        :param p1: first point
        :param p2: second point
        :return: distance as a float
        """
        return((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        """
        computes the distance from the current point to another point
        :param p: AdvancedPoint instance
        :return: distance as a float
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
