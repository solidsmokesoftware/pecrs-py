=====
Space
=====

The Space handles the positions and collisions of Shapes in an optimized way. Shapes are added to a SpatialHash which is used to reduce the number of collision detection events. 
Once added to the Space, Shapes can be moved, pushed, or placed and collide with other Shapes.

.. code-block:: python

   from pecrs.space import Space
   from pecrs.shape import Rect

   space = Space()

   shapeA = Rect(0, 0, 32, 32)
   shapeB = Rect(0, 0, 32, 32)
   shapeC = Rect(0, 0, 32, 32)

   space.add(shapeA)
   space.add(shapeB)
   space.add(shapeC)

   space.check_at(0, 0) #True, collisions
   space.check(shapeA) #True, collisions
   space.check_two(shapeA, shapeB) #True, colliding

   space.collisions_at(0, 0) #[shapeA, shapeB, shapeC] list of all collisions
   space.collisions_with(shapeA) #[shapeB, shapeC] list of all collisions

   space.move(shapeA, 1, 0, 100) #Move shapeA 1 in the x(Left) for 100 units
   space.push(shapeB, 100, 0) #Push shapeB 100 in the x(Left)
   space.place(shapeC, -10, -10) #Place shapeC at -10 x, -10 y)
