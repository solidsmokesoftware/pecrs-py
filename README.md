![logo](https://raw.githubusercontent.com/solidsmokesoftware/pecrs-py/master/logo.png)

# Pythonic Entity Collision Resolution System

pecrs is a pure Python 2D physics system with a focus on top-down games and simple platformers. 

Pure Python makes pecrs portable and easy to modify to suit your own needs.

Focused use-case makes pecrs simple to learn and use.

# Installation

Via pip

`python -m pip install pecrs`

# Quickstart
```python

from pecrs import *


id = 0
position = Vector(100, 500)
shape = Rect(10, 10)
body = Body(id, position, shape)

id = 1
position_other = Vector(100, 495)
other = Body(id, position_other, shape)

spatial_hash_size = 128
space = Space(spatial_hash_size)

space.add(body)
space.add(other)

collision = space.check(body)
print(f"Are 0 and 1 colliding? {collision}")
```

# Structual Overview

The base functionality of pecrs is provided by Vector, Shape, SpatialHash, and Index. Vector and Shape are datatypes for describing a Body. SpatialHash keeps track of a collection of objects based on position, while Index keeps track of indentification numbers for Bodies.

At the core level of operations are Bodies and the Collider. A Body consists of a Shape, a position(Vector), and an id(Provided by Index) and is the key unit of simulation. The Collider works with Shapes and Vectors to detect intersections.

Above that exists the Space. The Space manages Bodies in a SpatialHash and detects collisions within via the Collider.

At the highest level exists the Controller. The Controller creates Bodies in a Space and handles their interactions, as well as the physics simulation itself. The Controller is follows Object-Oriented design principles and provides callbacks into all of its functionality that can be easily extended. 

# Real-world Usage
```python

from pecrs.controller import Controller
from pecrs.body import Body
from pecrs.shape import Rect


class Player(Body):
   def __init__(self, id, position):
      shape = Rect(32, 32)
      super().__init__(id, position, shape)
      self.name = "player"
      self.speed = 100
      self.moving = True


class Objects(Controller):
   def __init__(self, collision_area_size):
      super().__init__(collision_area_size)
      self.factory["player"] = Player
      
   def on_make(self, body):
      print(f"Objects made {body.name} {body.id} at {body.position.x}:{body.position.y}")
      
   def on_motion(self, body):
      print(f"{body.name} {body.id} is at {body.position.x}:{body.position.y}")

   def on_collision(self, body, collisions):
      print(f"{body.name} is colliding with {len(collisions)} others")

objects = Objects(64)

playerA = objects.make(Player, 0, 0) # Bodies can be made with thier class
playerB = objects.make_key("player", 10, 0) # Or with a key that can be communicated easily over networks

collision = objects.space.check_two(playerA, playerB)
if collision:
   print("Bodies A and B are colliding")

objects.place(playerA, 100, 0)
objects.move_to(playerB, 1, 0, 1)

objects.turn(playerA, 0, 1)
objects.move(playerA, 1)

collision = objects.space.check(playerA)
if collision:
   print("Body A is colliding with another body")

objects.delete(playerA)
objects.delete(playerB)

playerC = objects.make(Player, 0, 0, dx=1)
playerD = objects.make(Player, 0, 0, dx=-1)
playerE = objects.make(Player, 0, 0, dy =1)
playerF = objects.make(Player, 0, 0, dy =-1)

collisions = objects.space.get_body(playerC)
if collisions:
   print(f"Body C is colliding with {len(collisions)} others")

for i in range(10):
   objects.step(0.1)

```

# Documentation

https://solidsmokesoftware.github.io/pecrs/

# Demonstration

https://github.com/solidsmokesoftware/solconomy

![solconomy](https://camo.githubusercontent.com/de20b3b2014d20a8746f7346e777e323586d5a35/68747470733a2f2f692e696d6775722e636f6d2f566277677664372e706e67)

# Requirements

Tested with Python3.6.9
