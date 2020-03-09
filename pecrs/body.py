
from pecrs.shape import Rect

class AbsBody:
   """
   :param id: Identifer of the body, should be unique to an Index
   :param shape: Shape of the body
   :type shape: Shape

   The abstract base class for all bodies. Bodies are physical entities that can interact with other bodies in space.
   """
   def __init__(self, id, shape):
      self.id = id #: Identifer of the body, should be unique
      self.shape = shape #: Shape of the body.

      self.direction = (0, 0) #: Tuple(int, int), holds the direction the body moves in
      self.area = (0, 0) #: Tuple(int, int), the collision area the body is located in
      self.speed = 0 #: Number, how fast the body moves
      self.name = "absbody" #: string, used to communicate body type in a reader friendly way
      
      self.moving = False #: bool, If the body should be moved during processing
      

class Body(AbsBody):
   """
   :param id: Identifer of the body, should be unique
   :param shape: Physical Shape of the body
   :type id: int
   :type shape: Shape

   An active body. Extend Body for entities that move or think.
   """
   def __init__(self, id, shape):
      super().__init__(id, shape)


class StaticBody(AbsBody):
   """
   :param id: Identifer of the body, should be unique
   :param shape: Physical Shape of the body
   :type id: int
   :type shape: Shape

   A passive body. Extend StaticBody for entities that do not move or think.
   """
   def __init__(self, id, shape):
      super().__init__(id, shape)

    
