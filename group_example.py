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

      self.add(spriteA, moving=True)
      self.turn(spriteA, (150, 0))

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
