========
Collider
========

Collider provides the core functionality of pecrs by determining if shapes are colliding in abstract.
The Collider offers boolean collision detection between a variety of shapes with the ability to select the correct collision method if needed.
Collision methods use primiative types for collision testing to maximize flexability while having higher level interfaces for Shapes for greater easy of use.


.. code-block:: python

   from pecrs.collider import Collider

   collider = Collider()

   #First let's look at the low level collider functions.

   collider.rect_rect(32, 32, 0, 0, 32, 64, 10, 20) 
   #Tests for a collision between two Rects in abstract
   #The first is 32x32 at (0, 0)
   #The second is 32x64 at (10, 20)

   collider.rect_circle(32, 32, 0, 0, 64, -20, -40)
   #Same as before but between a rect and a circle.
   #Arguments after the rect describe a circle 64 units big at (-20, -40)
   #collider.circle_rect(...) is the same thing in reverse

   collider.circle_circle(32, 0, 0, 64, 0, 0)
   #Collision between two circles.

   #It's more practical to use higher level functions that accept Shapes instead of ints

   from pecrs.shape import *

   rectA = Rect(0, 0, 32, 32)
   rectB = Rect(10, 10, 32, 32)
   circleA = Circle(0, 0, 32)
   circleB = Circle(20, 20, 48)

   collider.check(rectA, rectB)
   #This method will figure out what Shapes are being used.
   #Since two Rects are being used, it will call collider.rect_rect()

   collider.check(rectA, circleB)
   #Also works. Resolves to collider.rect_circle()

   collider.check_rects(rectA, rectB)
   #Use this if you already know what your Shapes are.

   collider.check_circles(circleA, circleB)
   #For two circles
