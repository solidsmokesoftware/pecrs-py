=======================
Integrating with Pyglet
=======================

In order to work seamlessly with Pyglet, pecrs.Rect() was modeled after pyglet.sprite.Sprite(). Through the power of ducktyping, this allows Pyglet Sprites to work interchangly in any place you could use a pecrs Rect.
Specifically, Collider.check_rects(), Collider.rect_rect(), and all methods in Space(). When using a Sprite as a Rect, placement is handled by Sprite.position, and dimensions are covered by Sprite.width and Sprite.height.
As the Sprite is added to a Space, it will be given an .area made up Tuple(Int, Int) representing the collision area in space the shape occupies. At the highest level of abstraction, pecrs uses Bodies which have a Shape. Again Pyglet Sprites can be used interchangly with Rects. 

Caveat: Collider.check() will not work with Sprites as Shapes. It uses typing to determine the appropriate collider methods to use, which will not recognize the Sprites.