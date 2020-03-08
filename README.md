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

from pecrs import *

controller = Controller()
bodyA = controller.make(Body, 0, 0, 32, 32)
bodyB = controller.make(Body, 10, 0, 32, 32)

collision = controller.space.check_body(bodyA)
print(f"Is something colliding with bodyA? {collision}")

collisions = controller.space.collisions_with(bodyB)
print(f"Who is colliding with bodyB? {collisions}")

controller.place(bodyB, 100, 0)

collision = controller.space.check_bodies(bodyA, bodyB)
print(f"Are bodyA and bodyB colliding? {collision}")
```

# Structual Overview

The core functionality of pecrs is provided by Shapes. Shape are datatypes for describing the physical properties of a Body. 

At the intermediate level of organization are Bodies and the Collider. A Body consists of a Shape and an id(Provided by Index) and is the cornerstone unit of simulation. The Collider works with Shapes or Bodies to detect intersections.

Above that exists the Space. The Space optimizes collision detection using a Spatialhash.

At the highest level exists the Controller. The Controller creates Bodies in a Space and handles their interactions, as well as the physics simulation itself. The Controller is follows Object-Oriented design principles and provides callbacks into all of its functionality that can be easily extended. 

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
      self.make_with(Dude, sprite, dx=dx, dy=dy)

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
