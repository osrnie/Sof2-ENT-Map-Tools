from Points import *

## Setting a default point (0,0,0) ##
DEF_POINT = Point()

## Spits the points for debugging ##
def spit(arr):
    print(f"List length: {len(arr)}")
    for i in range(len(arr)):
        print(arr[i].toString())


def toEnt(arr, **properties):
	pts = ''
	txt = ''
	for name, value in properties.items():
		pts += (f'\"{name}\" \"{value}\"\n')
	
	for i in range(len(arr)):
		txt += (f'{{\n'
						f'{pts}'
						f'\"origin\" {arr[i].toString()}\n'
						f'}}\n')
		
	return txt
	


# Debugging:

r1 = duplicate(fillRectangle(Point(), Point(10,10,10), Point(), False), Point(100,100,100), 2)

print(len(r1))
print(toEnt(r1, classname = 'test', spawnflags = 2))
#spit(r1)





