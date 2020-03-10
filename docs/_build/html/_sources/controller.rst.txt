==========
Controller
==========

Controller offers high-level influence over Bodies in a Space.
In addition to the Space, the Controller has an Index to keep track of bodies, and keeps tracks of which Bodies are Static for optimization purposes.

.. code-block:: python

   from pecrs.controller import Controller
   from pecrs.body import Body

   controller = Controller()

   bodyA = controller.make(Body, 0, 0, 32, 32)
   bodyB = controller.make(Body, 0, 0, 32, 32)
   bodyC = controller.make(Body, 0, 0, 32, 32)
   
   controller.check_at(0, 0) #True, collisions
   controller.check(bodyA) #True, collisions
   controller.check_two(bodyA, bodyB) #True, colliding

   controller.collisions_at(0, 0) #[bodyA, bodyB, bodyC] list of all collisions
   controller.collisions_with(bodyA) #[bodyB, bodyC] list of all collisions

   controller.move(bodyA, 1, 0, 100) #Move bodyA 1 in the x(Left) for 100 units
   controller.push(bodyB, 100, 0) #Push bodyB 100 in the x(Left)
   controller.place(bodyC, -10, -10) #Place bodyC at -10 x, -10 y)

   controller.step(0.1)
