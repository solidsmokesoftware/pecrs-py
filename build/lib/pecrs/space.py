
from pecrs.spatialhash import SpatialHash
from pecrs.collider import Collider


class Space:
   """
   :param size: Size pf the collision areas
   :type size: int

   Space handles the interactions between the SpatialHash and the Collider.
   You can change the values here to work with different spatial partioning system and collision systems.
   """

   def __init__(self, size):
      self.grid = SpatialHash(size) #: SpatialHash, spatial partitioning system. Think about combining these into one class
      self.collider = Collider() #: Collider, collision detection system

   def add(self, body, area=None):
      """
      :param body: Body to add to the space
      :param area: Area of the space to add the body to. Calculate from body.position if None
      :type body: AbsBody
      :type area: tuple(int, int) or None
      
      Adds a body to the space.
      Bodies are added to their collision area as well as the 8 nearest neighboring cells to handle overlap and fast moving obejcts.
      """
      if area:
         x_area = area[0]
         y_area = area[1]
      else:
         body.area = self.grid.scale(body.position.x, body.position.y)
         x_area = body.area[0]
         y_area = body.area[1]

      self.grid.add(body, (x_area-1, y_area-1))
      self.grid.add(body, (x_area, y_area-1))
      self.grid.add(body, (x_area+1, y_area-1))
      self.grid.add(body, (x_area-1, y_area))
      self.grid.add(body, (x_area, y_area))
      self.grid.add(body, (x_area+1, y_area))
      self.grid.add(body, (x_area-1, y_area+1))
      self.grid.add(body, (x_area, y_area+1))
      self.grid.add(body, (x_area+1, y_area+1))

   def delete(self, body, area=None):
      """
      :param body: Body to removed from the space
      :param area: Area of the space to remove the body from. Calculate from body.position if None
      :type body: AbsBody
      :type area: tuple(int, int) or None

      Removes a body from the space.
      """
      if area:
         x_area = area[0]
         y_area = area[1]
      else:
         x_area = body.area[0]
         y_area = body.area[1]

      self.grid.delete(body, (x_area-1, y_area-1))
      self.grid.delete(body, (x_area, y_area-1))
      self.grid.delete(body, (x_area+1, y_area-1))
      self.grid.delete(body, (x_area-1, y_area))
      self.grid.delete(body, (x_area, y_area))
      self.grid.delete(body, (x_area+1, y_area))
      self.grid.delete(body, (x_area-1, y_area+1))
      self.grid.delete(body, (x_area, y_area+1))
      self.grid.delete(body, (x_area+1, y_area+1))

   def has(self, body):
      """
      :param body: Body to check for
      :type body: AbsBody
      :return: True if the space contains the body, False if not
      :rtype: bool

      Checks if a space has a body in that body's area
      Note that the body's must be set correctly or errors can occur
      """
      return self.grid.has(body, body.area)

   def get(self, position, shape):
      """
      :param position: Position to search
      :param shape: Shape to use for collision detection
      :type position: Vector
      :type shape: Shape
      :return: List of bodies colliding at the position
      :rtype: list(AbsBody)

      Gets a list of all bodies colliding with shape at position
      """
      area = self.grid.scale(position.x, position.y)
      collisions = []
      bucket = self.grid.get(area)
      for body in bucket:
         if self.collider.check(shape, position, body.shape, body.position):
            collisions.append(body)
      return collisions

   def get_body(self, body):
      """
      :param body: Body to find collisions for
      :type body: AbsBody
      :return: List of bodies colliding at the position
      :rtype: list(AbsBody)

      Get a list of all bodies colliding with body
      """
      collisions = []
      for other in self.grid.get(body.area):
         if body.id != other.id:
            if self.check_two(body, other):
               collisions.append(other)
      return collisions
      
   def check_two(self, body, other):
      """
      :param body: First body to check for collision
      :param other: Second body to check for a collision
      :type body: AbsBody
      :type other: AbsBody
      :return: True if the two bodies are colliding, False if not
      :rtype: bool

      Check to see if two bodies are colliding with each other in abstract. Does not use the space.
      """

      if body.id != other.id:
         if self.collider.check(body.shape, body.position, other.shape, other.position):
            return True
         else:
            return False
      else:
         return False
   
   def check(self, body):
      """
      :param body: Body to check for collisions
      :type body: AbsBody
      :return: True if the body is colliding with anything in space, False if not
      :rtype: bool

      Check to see if something is colliding with body in the space.
      """
      for other in self.grid.get(body.area):
         if self.check_two(body, other):
            return True
      return False

   def move(self, body, dir):
      """
      :param body: Body to add to the space
      :param dir: Direction to move the body in
      :type body: AbsBody
      :type dir: Vector

      Moves a body. This will be more efficent than place
      TODO Not implemented yet. Use place(body, area) instead
      """
      return

   def place(self, body, area):
      """
      :param body: Body to be moved from the space
      :param area: Area of the space to move the body to
      :type body: AbsBody
      :type area: tuple(int, int)

      Moves a body from one collision area to another
      """
      self.delete(body, area)
      body.area = area
      self.add(body, area)

