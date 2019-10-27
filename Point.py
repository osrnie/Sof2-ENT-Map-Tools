# Create a 3 dimensional point on x, y & z axes
class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def toString(self):
        return (f"\"{self.x} {self.y} {self.z}\"")  ## "x y x"

DEF_POINT = Point()