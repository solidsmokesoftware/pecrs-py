
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
