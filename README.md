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
print(f"Are rectA and rectB colliding? {collision}")
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


class Dude(pyglet.sprite.Sprite):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.id = None
      self.speed = 100
      self.moving = True
      self.direction = None
      self.area = None


class Objects(Controller):
   def __init__(self, batch):
      super().__init__()
      self.batch = batch
      self.blue_image = pyglet.resource.image("blue_rect.png")
      self.red_image = pyglet.resource.image("red_rect.png")

   def make_dude(self, x, y, dx=0, dy=0):
      body = Dude(self.blue_image, x=x, y=y, batch=self.batch)
      body.direction = (dx, dy)
      self.add(body)

   def on_collision(self, body, collisions):
      body.image = self.red_image
      

class Game:
   def __init__(self):
      self.window = pyglet.window.Window(400, 300)
      self.batch = pyglet.graphics.Batch()

      self.objects = Objects(self.batch)
      self.objects.make_dude(0, 150, dx=1)
      self.objects.make_dude(300, 150)

      pyglet.clock.schedule_interval(self.run, 1.0/60)
      pyglet.app.run()

   def run(self, delta):
      self.objects.step(delta)
      self.window.clear()
      self.batch.draw()

game = Game()
```

# Documentation

https://solidsmokesoftware.github.io/pecrs-py/

# Demonstration

(Currently broken)

https://github.com/solidsmokesoftware/solconomy

![solconomy](https://camo.githubusercontent.com/de20b3b2014d20a8746f7346e777e323586d5a35/68747470733a2f2f692e696d6775722e636f6d2f566277677664372e706e67)

# Requirements

Tested with Python3.6.9
