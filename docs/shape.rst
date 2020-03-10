=====
Shape
=====

Shapes are the most basic unit used by pecrs. 
A Shape represents a physical object on a two-dimensional plane. 
All Shapes have a position, and most Shapes will have one or more dimensions or physical characteristics.

The most common shape used is the Rect(). 
A Rect is an axis-aligned bounding box, which means that it does not rotate.
Rects are the fastest shape to resolve collisions for.
They have a width and a height which extends to the left and up of the position, respectively.

Circles are slower to collide but can provide for more accurate collision shapes.
They have a radius which extends out from the position.

Because Python is ducktyped, anything that has the signature of a Shape can effectively be used as a Shape.
In particular, Pyglet Sprites have a position, width, and height and thus can be used as Rects in almost every method that accepts a Rect.
Notable exception being Collider.check()


.. code-block::python

   from pecrs.shape import Rect
   from pecrs.shape import Circle
   from pecrs.shape import Shape
   #from pecrs.shape import * would also be fine if using multiple shapes

   r = Rect(0, 0, 32, 64) # Creates a Rect at (0, 0) with a width of 32 and a height of 64
   c = Circle(0, 100, 12) # Creates a Circle at (0, 100) with a radius of 12

   if isinstance(r, Shape):
      print("r is a Shape")
   
   print(f"r is a {r.position})
   print(f"r is {r.width} pixels wide and {r.height} pixels tall"})


