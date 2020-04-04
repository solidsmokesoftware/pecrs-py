![logo](https://raw.githubusercontent.com/solidsmokesoftware/pecrs-py/master/logo.png)

# Pythonic Entity Collision Resolution System

pecrs is a pure Python 2D physics system with a focus on top-down games and simple platformers. 

Pure Python makes pecrs portable and easy to modify to suit your own needs.

Focused use-case makes pecrs simple to learn and use.

[Seamless integration](https://solidsmokesoftware.github.io/pecrs-py/pyglet.html) with [Pyglet](http://pyglet.org/)

# Installation

Via pip

`python3 -m pip install pecrs`

# Quickstart
```python

from pecrs import *

space = Space()
rectA = Rect(0, 0, 32, 32)
rectB = Rect(10, 0, 32, 32)

space.add(rectA)
space.add(rectB)

collision = space.check(rectA)
print(f"Is something colliding with rectA? {collision}")

collisions = space.collisions_with(rectB)
print(f"Who is colliding with rectB? {collisions}")

space.place(rectB, 100, 0)

collision = space.check_two(rectA, rectB)
print(f"Are rectA and rectB still colliding? {collision}")
```

# Structual Overview

Base types of the system are Shapes and Bodies. 
Shapes have a position and dimensions which describe its physical properties.
Bodies are Shapes with an id, direction, speed, and movement state.

Core functionality is providied by the Collider, which detects collisions between Shapes or Shape-like Objects.

The Space handles positioning of Shapes and optimizes collision handling.

The Controller provides high-level object oriented control over Bodies in a Space.

# Real-world Usage

![demo](https://raw.githubusercontent.com/solidsmokesoftware/pecrs-py/master/pyglet_demo.gif)

```python

from pecrs import *
import pyglet


class World(Space):
   def __init__(self):
      super().__init__()
      self.window = pyglet.window.Window(400, 300)
      self.batch = pyglet.graphics.Batch()
      
      self.red_image = pyglet.resource.image("red_rect.png")
      self.blue_image = pyglet.resource.image("blue_rect.png")

      spriteA = pyglet.sprite.Sprite(self.blue_image, x=0, y=150, batch=self.batch)
      spriteB = pyglet.sprite.Sprite(self.blue_image, x=300, y=150, batch=self.batch)

      self.add(spriteA)
      self.turn(spriteA, (150, 0))
      self.start_moving(spriteA)

      self.add(spriteB)
      
      pyglet.clock.schedule_interval(self.run, 1.0/60)
      pyglet.app.run()

   def on_collision(self, shape, collisions):
      shape.image = self.red_image

   def run(self, delta):
      self.step(delta)
      self.window.clear()
      self.batch.draw()

world = World()
```

# Documentation

https://solidsmokesoftware.github.io/pecrs-py/

# Demonstration

https://github.com/solidsmokesoftware/solconomy

![solconomy](https://camo.githubusercontent.com/de20b3b2014d20a8746f7346e777e323586d5a35/68747470733a2f2f692e696d6775722e636f6d2f566277677664372e706e67)

# Requirements

Tested with Python3.6.9
