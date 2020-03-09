![logo](https://raw.githubusercontent.com/solidsmokesoftware/pecrs-py/master/logo.png)

# Pythonic Entity Collision Resolution System

pecrs is a pure Python 2D physics system with a focus on top-down games and simple platformers. 

Pure Python makes pecrs portable and easy to modify to suit your own needs.

Focused use-case makes pecrs simple to learn and use.

Seamless integration with Pyglet

# Installation

Via pip

`python3 -m pip install pecrs`

# Quickstart
```python

controller = Controller()
bodyA = controller.make(Body, 0, 0, 32, 32)
bodyB = controller.make(Body, 10, 0, 32, 32)

collision = controller.check(bodyA)
print(f"Is something colliding with bodyA? {collision}")

collisions = controller.collisions_with(bodyB)
print(f"Who is colliding with bodyB? {collisions}")

controller.place(bodyB, 100, 0)

collision = controller.check_two(bodyA, bodyB)
print(f"Are bodyA and bodyB colliding? {collision}")
```

# Structual Overview

Base type of the system are Shapes. Shapes have a position and dimensions which describe its physical properties.

Core functionality is providied by the Collider, which detects collisions between Shapes in abstract.

The Space handles positioning of Shapes and optimizes collision handling.

The Controller provides high-level object oriented control over Bodies in a Space.

# Real-world Usage

![demo](https://raw.githubusercontent.com/solidsmokesoftware/pecrs-py/master/pyglet_demo.gif)

```python

from pecrs import *
import pyglet


class Dude(Body):
   def __init__(self, id, sprite):
      super().__init__(id, sprite)
      self.speed = 100
      self.moving = True


class Objects(Controller):
   def __init__(self, batch):
      super().__init__()
      self.batch = batch
      self.blue_image = pyglet.resource.image("blue_rect.png")
      self.red_image = pyglet.resource.image("red_rect.png")

   def make_dude(self, x, y, dx=0, dy=0):
      sprite = pyglet.sprite.Sprite(self.blue_image, x=x, y=y, batch=self.batch)
      self.make_from(Dude, sprite, dx=dx, dy=dy)

   def on_collision(self, body, collisions):
      body.shape.image = self.red_image
      

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
