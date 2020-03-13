
from pecrs.spatialhash import SpatialHash
from pecrs.collider import Collider

class Space:
   """
   :param size: Size of the collision areas
   :type size: int

   Space handles the movement and collision detection between shapes.
   You can change the values here to work with different spatial partioning system and collision systems.
   """

   def __init__(self, size=256):
      self.grid = SpatialHash(size) #: SpatialHash, spatial partitioning system. Think about combining these into one class
      self.collider = Collider() #: Collider, collision detection system

   def add(self, shape, update_area=True):
      """
      :param shape: Shape to add to the space
      :type shape: Shape
      
      Adds a shape to the space.
      Bodies are added to their collision area as well as the 8 nearest neighboring cells to handle overlap and fast moving obejcts.
      """
      if update_area:
         shape.area = self.grid.scale(shape.position[0], shape.position[1])

      x_area = shape.area[0]
      y_area = shape.area[1]

      self.grid.add(shape, (x_area-1, y_area-1))
      self.grid.add(shape, (x_area, y_area-1))
      self.grid.add(shape, (x_area+1, y_area-1))
      self.grid.add(shape, (x_area-1, y_area))
      self.grid.add(shape, (x_area, y_area))
      self.grid.add(shape, (x_area+1, y_area))
      self.grid.add(shape, (x_area-1, y_area+1))
      self.grid.add(shape, (x_area, y_area+1))
      self.grid.add(shape, (x_area+1, y_area+1))

   def delete(self, shape):
      """
      :param shape: Shape to removed from the space
      :type shape: Shape

      Removes a shape from the space.
      """
      x_area = shape.area[0]
      y_area = shape.area[1]

      self.grid.delete(shape, (x_area-1, y_area-1))
      self.grid.delete(shape, (x_area, y_area-1))
      self.grid.delete(shape, (x_area+1, y_area-1))
      self.grid.delete(shape, (x_area-1, y_area))
      self.grid.delete(shape, (x_area, y_area))
      self.grid.delete(shape, (x_area+1, y_area))
      self.grid.delete(shape, (x_area-1, y_area+1))
      self.grid.delete(shape, (x_area, y_area+1))
      self.grid.delete(shape, (x_area+1, y_area+1))

   def has(self, shape):
      """
      :param shape: Shape to check for
      :type shape: Shape
      :return: True if the space contains the shape, False if not
      :rtype: bool

      Checks if a space has a shape in that shape's area
      Note that the shape's must be set correctly or errors can occur
      """
      try:
         return self.grid.has(shape, shape.area)
      except AttributeError:
         return False

   def collisions_at(self, x, y, width=1, height=1):
      """
      :param x: Posistion to search for on the x-axis
      :param y: Posistion to search for on the y-axis
      :param width: Width of the search area
      :param height: Height of the search area
      :type x: Int
      :type y: Int
      :type width: Int
      :type height: Int
      :return: List of shapes colliding at the position
      :rtype: list(Shapes)

      Gets a list of all shapes colliding at x, y
      """
      area = self.grid.scale(x, y)
      collisions = []
      for shape in self.grid.get(area):
         if self.collider.rect_rect(width, height, x, y, shape.width, shape.height, shape.position[0], shape.position[1]):
            collisions.append(shape)
      return collisions

   def collisions_with(self, shape):
      """
      :param shape: Shape to find collisions with
      :type shape: Shape
      :return: List of shapes colliding at the position
      :rtype: list(Shape)

      Get a list of all shapes colliding with shape
      """
      collisions = []
      for other in self.grid.get(shape.area):
         if shape != other:
            if self.collider.check_rects(shape, other):
               collisions.append(other)
      return collisions
      
   def check_at(self, x, y, width=1, height=1):
      """
      :param x: Posistion to search for on the x-axis
      :param y: Posistion to search for on the y-axis
      :param width: Width of the search area
      :param height: Height of the search area
      :type x: Int
      :type y: Int
      :type width: Int
      :type height: Int
      :return: True if there is a collision at x, y, False if not
      :rtype: bool

      Check to see if there is a collision at x, y in space.
      """
      area = self.grid.scale(x, y)
      for shape in self.grid.get(area):
         if self.collider.rect_rect(width, height, x, y, shape.width, shape.height, shape.position[0], shape.position[1]):
            return True
      return False
      
   def check(self, shape):
      """
      :param shape: Shape to check for collisions
      :type shape: Shape
      :return: True if the shape is colliding with anything in space, False if not
      :rtype: bool

      Check to see if something is colliding with shape in the space.
      """
      for other in self.grid.get(shape.area):
         if shape != other:
            if self.collider.check_rects(shape, other):
               return True
      return False

   def check_two(self, shape, other):
      """
      :param shape: First Shape to check for collision
      :param other: Second Shape to check for collision
      :type shape: Shape
      :type other: Shape
      :return: True if the two shapes are colliding, False if not
      :rtype: Bool

      Check to see if two shapes are colliding
      """
      return self.collider.check_rects(shape, other)

   def update_area(self, shape):
      """
      :param shape: Body to be moved from the space
      :param area: Area of the space to move the shape to
      :type shape: AbsBody
      :type area: Tuple(Int, Int)
      :return: Original area if updating, None if not
      :rtype: Tuple(Int, Int) or None

      Moves a shape from one collision area to another
      """
      area = self.grid.scale(shape.position[0], shape.position[1])
      if shape.area != area:
         self.delete(shape)
         start = shape.area
         shape.area = area
         self.add(shape, False)
         return start
      else:
         return None
      
   def move(self, shape, x, y, distance):
      """
      :param shape: Shape to move
      :param x: Direction to move in on horizontal plane
      :param y: Direction to move in on the vertical plane
      :param distance: Distance to move for
      :type shape: Shape
      :type x: int
      :type y: iny
      :type distance: float
      :return: Distance moved
      :rtype: tuple(int, int)
      
      Advances a shape in the direction x, y for distance units.
      """
      xstep = int(x * distance)
      ystep = int(y * distance)
      shape.position = (shape.position[0]+xstep, shape.position[1]+ystep)
      return (xstep, ystep)

   def push(self, shape, x, y):
      """
      :param shape: Shape to push
      :param x: Direction on the horizontal plane to push the shape
      :param y: Direction on the vertical plane to push the shape
      :type shape: Shape
      :type x: int
      :type y: int

      Pushes a shape in the direction of x, y in space
      """
      shape.position = (shape.position[0]+x, shape.position[1]+y)

   def place(self, shape, x, y):
      """
      :param x: The position in space to place the shape on the horizontal plane
      :param y: The position in space to place the shape on the vertical plane
      :type x: int
      :type y: int

      Directly places a shape at x, y in space
      """
      shape.position = (x, y)
      
