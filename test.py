from ent import *


# Spits the points for debugging
def spit(arr):
    print(f"List length: {len(arr)}")
    for i in range(len(arr)):
        print(arr[i].toString())



p1 = Point()
p2 = Point(10,0,0)
offset = Point(5, 5, 5)

cube = duplicate(fillRectangle(p1,p2, offset, False), Point(100,100,100), 1)
output = toEnt(cube, classname='bspmodel', angle='0 0 0', modelname='instances/colombia/npc_jump1')
print(output)



x = re.findall(r'"origin" ".*"' ,output)
for i in x:
	break
print(x)

