import random

class Point:
    def _init_(self, x, y):
        """
        Initialize a point object.
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x
        self.y = y

    def _str_(self):
        """
        Magic method that is called when we try to print an instance
        :return: <x,y>
        """
        return f"p({self.x}, {self.y})"

    def _repr(self):  # Fixed __repr_ method
        return self._str_()

    def distance_orig(self):
        """
        Calculate distance from the origin using Euclidean distance formula.
        :return: Distance from (0,0)
        """
        return (self.x * 2 + self.y * 2) ** 0.5  # Fixed distance calculation

    def _lt_(self, other):
        """
        Define sorting order by distance from origin.
        """
        return self.distance_orig() < other.distance_orig()


p = Point(1, 2)
p2 = Point(2, 3)
p4 = Point(4.4, -55)

print(f"p.x={p.x} and p.y={p.y}")
print(f"p4.x={p4.x} and p4.y={p4.y}")
p.x = 20
print(f"p.x={p.x} and p.y={p.y}")
print(p)

points = []
for i in range(5):
    points.append(Point(random.randint(-10, 10), random.randint(-10, 10)))

print("I got these 5 random points:")
for p in points:
    print(p)

points.sort()
print("Sorted points by distance from origin:")
print(points)

p = Point(3, 4)
print(f"Distance from origin: {p.distance_orig()}")
p2= Point(1,1)
print(f'i am comparig p > p2 {p>p2}')
print('the sorted list of points is:')
points.sort()
print(points)