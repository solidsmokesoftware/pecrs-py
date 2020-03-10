=======================
Integrating with Pyglet
=======================

In order to work seamlessly with Pyglet, Shapes in pecrs were modeled after pyglet.sprite.Sprite(). 
Through the power of ducktyping, this allows Pyglet Sprites to work interchangly in any place you could use a pecrs Rect().
Specifically, Collider.check_rects(), Collider.rect_rect(), and all methods in Space(). When using a Sprite as a Rect, placement is handled by Sprite.position, and dimensions are covered by Sprite.width and Sprite.height.
As the Sprite is added to a Space, it will be given an .area made up Tuple(Int, Int) representing the collision area in space the shape occupies. 


At the highest level of abstraction, pecrs uses Bodies which extend from Shapes. 
Subclassing pyglet.sprite.Sprite instead of Rect allows a Sprite to function as a Body with the Controller.

Caveat: Collider.check() will not work with Sprites as Shapes. It uses typing to determine the appropriate collider methods to use, which will not recognize the Sprites.

.. code-block:: python

   import pyglet
   from pecrs import *

   space = Space()
   collider = Collider()

   shape = Rect(0, 0, 32, 32)

   img = pyglet.image.load(path)
   sprite = pyglet.sprite.Sprite(img, x=0, y=0)

   collider.check_rects(shape, sprite) #True, they're colliding
   collider.collisions_at(0, 0) #[shape, sprite] List of all Shapes colliding at 0, 0
   collider.collisions_with(sprite) #[shape] List of all Shapes colliding with sprite

   space.add(shape)
   space.add(sprite)

   space.place(sprite, 100, 100)

   space.check(sprite) #False, no collisions
   space.collisions_with(sprite) #[] no collisions
   space.collisions_at(100, 100) #[sprite] colliding with sprite at 100, 100

