
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

   def move(self, delta):
      """
      :param delta: Amount of time to move for
      :type delta: float
      :return: Distance moved
      :rtype: tuple(int, int)

      Advances a body by its speed in its directions for delta units of time

      Using this directly only updates the body and not any associated space systems.
      It's reccomended to use Controller.move(body, delta) instead to manage collision areas.
      """

      step = self.speed * delta
      xstep = int(self.direction[0] * step)
      ystep = int(self.direction[1] * step)
      self.shape.position = (self.shape.position[0]+xstep, self.shape.position[1]+ystep)
      return (xstep, ystep)
 
   def move_to(self, x, y, delta):
      """
      :param x: Direction to move in on horizontal plane
      :param y: Direction to move in on the vertical plane
      :param delta: Amount of time to move for
      :type x: int
      :type y: iny
      :type delta: float
      :return: Distance moved
      :rtype: tuple(int, int)
      
      Advances a body by its speed in the direction x, y of delta units of time

      Using this directly only updates the body and not any associated space systems.
      It's reccomended to use Controller.move_to(body, x, y) instead to manage collision areas.
      """
      step = self.speed * delta
      xstep = int(x * step)
      ystep = int(y * step)
      self.shape.position = (self.shape.position[0]+xstep, self.shape.position[1]+ystep)
      return (xstep, ystep)

   def push(self, x, y):
      """
      :param x: Direction on the horizontal plane to push the body
      :param y: Direction on the vertical plane to push the body
      :type x: int
      :type y: int

      Pushes a body in the direction of x, y
      
      Using this directly only updates the body and not any associated space systems.
      It's reccomended to use Controller.push(body, x, y) instead to manage collision areas.
      """
      self.shape.position = (self.shape.position[0]+x, self.shape.position[1]+y)

   def place(self, x, y):
      """
      :param x: The position in space to place the body on the horizontal plane
      :param y: The position in space to place the body on the vertical plane
      :type x: int
      :type y: int

      Directly places a body at x, y
      
      Using this directly only updates the body and not any associated space systems.
      It's reccomended to use Controller.push(body, x, y) instead to manage collision areas.
      """
      self.shape.position = (x, y)


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

    
