from EntFormat import *


# A function to duplicate an array and moving it by a set offset on each axis
def duplicate(arr, offset, times):
    tArr = []  # Temporary array
    buffer = arr  # Buffer to keep the currently active array

    # Nested loop that pushes all the points into a buffer then combine it with the original list
    for i in range(times):
        for j in range(len(buffer)):
            tArr.append(Point(buffer[j].x + offset.x, buffer[j].y + offset.y, buffer[j].z + offset.z))
        arr.extend(tArr)
        buffer = tArr
        tArr.clear()
    return arr


# Spits the points for debugging
def spit(arr):
    print(f"List length: {len(arr)}")
    for i in range(len(arr)):
        print(arr[i].toString())




