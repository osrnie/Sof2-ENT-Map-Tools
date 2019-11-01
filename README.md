# Sof2-ENT-Map-Tools
Generate .ent objects for SOF2 maps easier

## API Documentation:
- **Point**(x, y, z):
  Class for making a coordinate in the space takes 3 integers (/viewpos in-game)

- **fillRectangle**(point, point, offset, outline):
  * A function that takes 2 corners of a rectangle an offset and a boolean for outlining.
  * **Offset**: the distance between points in the rectangle for each axis (x, y & z).
  * **Outline**: while true, will hollow the shape (default = True).
    
  for example:
    here, the 2 corners could be any opposite corners of the rectangle, i.e (p1,p8) (p3,p6) etc....
    p6 -- p8
    p5 -- p7
    p2 -- p4
    p1 -- p3
    
 - **duplicate**(array, offset, times):
    * A functin that duplicates an array and increments its values with defined offset.
    * **array**: Represent the shape you created earlier.
    * **offset**: the offset of the shape as a whole (affect all the objects in the shape).
    * **times**: number of times to duplicate the array and add the offsets each time.
  
  
 - **toEnt**(array, properties):
    * A function that format the finished array to represent actual Entity codes (for the .ent files)
    * **array**: the finished shape & its duplicates as a single array
    * **properties**: all the different entity keys, this is a \**kwarg (Keyword Argument), to use it first use the key as the variable and then equate it to its value, for example:
    `classname = 'misc_bsp'` will output: `"classname" "misc_bsp"`
