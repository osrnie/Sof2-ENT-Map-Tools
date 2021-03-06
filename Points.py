class Point:
    def __init__(self, x=0, y=0, z=0):
    	try:
    		self.x = int(x) 
    		self.y = int(y)
    		self.z = int(z)
    	except:
    		return 'One of your Point parameters was not a number! setting 0 as defaults'
    		self.x = 0 
    		self.y = 0
    		self.z = 0
    		
    def toString(self):
        return f'\"{self.x} {self.y} {self.z}\"'


# Getting 2 points (corners of a rectangle) and offsets for each axis and filling the missing points in the rectangle
# according to the offset
def fillRectangle(p1=Point(), p2=Point(), offset=Point(), outline=bool(True)):
    # Rotating the corners to fixed positions opposite each other:
    p1 = Point(min(p1.x, p2.x), min(p1.y, p2.y), min(p1.z, p2.z))
    p2 = Point(max(p1.x, p2.x), max(p1.y, p2.y), max(p1.z, p2.z))

    # Defaults the offset to the cube corners
    if offset.x == 0:
        offset.x = p2.x
    if offset.y == 0:
        offset.y = p2.y
    if offset.z == 0:
        offset.z = p2.z

    points = []

    # Nesting each axis list into a 3D array
    for i in range(p1.z, p2.z + 1, offset.z):
        for j in range(p1.y, p2.y + 1, offset.y):
            for k in range(p1.x, p2.x + 1, offset.x):
                points.append(Point(k, j, i))

    # Removes all the inner points leaving only the outline in the list (Taking into account that the list is sorted
    # from the min to max)
    if outline:
        buffer = []
        for i in range(len(points)):
            if points[i].x == p1.x or points[i].x == p2.x or points[i].y == p1.y or points[i].y == p2.y or points[
                i].z == p1.z or points[i].z == p2.z:
                buffer.append(points[i])

        points = buffer

    return points


# A function to duplicate an array and moving it by a set offset on each axis
def duplicate(arr, offset=Point(100, 100, 100), times=2):
    length = len(arr)
    buffer = []
    temp = arr.copy()

    for i in range(times):
        for j in range(len(temp)):
            buffer.append(Point(temp[j].x + offset.x, temp[j].y + offset.y, temp[j].z + offset.z))

        arr.extend(buffer)
        temp = buffer.copy()

    return arr

