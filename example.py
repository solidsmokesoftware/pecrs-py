
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




