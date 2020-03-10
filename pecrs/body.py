
from pecrs.shape import Rect


class Body(Rect):
   """
   :param id: Identifer of the body, should be unique to an Index
   :param x: Position of the Body on the x-axis
   :type x: Int
   :param y: Position of the Body on the y-axis
   :type y: Int
   :param width: Width of the Body
   :type width: Int
   :param height: Height of the Body
   :type height: Int

   The abstract base class for all bodies. Bodies are physical entities that can interact with other bodies in space.
   """
   def __init__(self, id, x, y, width, height):
      super().__init__(x, y, width, height)
      self.id = id #: Identifer of the body, should be unique

      self.direction = (0, 0) #: Tuple(int, int), holds the direction the body moves in
      self.speed = 0 #: Number, how fast the body moves
      self.name = "absbody" #: string, used to communicate body type in a reader friendly way
      
      self.moving = False #: bool, If the body should be moved during processing
      
