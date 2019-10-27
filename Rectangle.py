from Point import *

# Given 2 Points as corners, generates a 3 dimensional rectangle with points based on the offsets
class Rectangle:
    def __init__(self, p1 = DEF_POINT, p2 = DEF_POINT, offsets = DEF_POINT):
        self.p1 = Point(min(p1.x, p2.x), min(p1.y, p2.y), min(p1.z, p2.z))
        self.p2 = Point(max(p1.x, p2.x), max(p1.y, p2.y), max(p1.z, p2.z))
        self.offsets = offsets
        self.points = []

        for i in range(p1.z, p2.z + 1, offsets.z):
            for j in range(p1.y, p2.y + 1, offsets.y):
                for k in range(p1.x, p2.x + 1, offsets.x):
                    self.points.append(Point(k, j, i))

    def outline(self):
        buffer = []
        for i in range(len(self.points)):
            if (self.points[i].x == self.p1.x or self.points[i].x == self.p2.x or self.points[i].y == self.p1.y or self.points[i].y == self.p2.y or self.points[i].z == self.p1.z or self.points[i].z == self.p2.z):
                buffer.append(self.points[i])

        self.points = buffer
        return self.points