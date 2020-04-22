
from pecrs.spatialhash import SpatialHash
from pecrs.collider import Collider
from pecrs.index import Index

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
      self.index = Index()
      self.ids = {}
      self.shapes = {}
      self.areas = {}
      self.moving = {}
      self.directions = {}
      self.actives = []
      self.groups = {}
      self.collidable = {}

   def add(self, shape, id=-1, collidable=True, active=True, moving=False, group=None):
      """
      :param shape: Shape to add to the space
      :type shape: Shape
      
      Adds a shape to the space.
      """
      if id < 0:
         id = self.index.next()
      self.ids[shape] = id
      self.shapes[id] = shape
      self.moving[shape] = moving
      area = self.grid.scale(shape.position[0], shape.position[1])   
      self.areas[shape] = area
      self.add_to_grid(shape, area)
      self.collidable[shape] = collidable
      
      if active:
         self.actives.append(shape)
         self.directions[shape] = (0, 0)
      
      if group:
         if group in self.groups:
            self.groups[group].append(shape)
         else:
            self.groups[group] = [shape]

   def delete(self, shape, group=None):
      """
      :param shape: Shape to removed from the space
      :type shape: Shape

      Removes a shape from the space.
      """
      if shape in self.ids:
         id = self.ids[shape]
         del self.ids[shape]
         del self.shapes[id]
         del self.moving[shape]
         self.delete_from_grid(shape, self.areas[shape])
         del self.areas[shape]
         if shape in self.actives: #TODO I think self.actives, self.directions might be work better with groups if given?
            self.actives.remove(shape)
         if shape in self.directions:
            del self.directions[shape]
         if group:
            self.groups[group].remove(shape)

   def delete_id(self, id, group=None):
      shape = self.ids[shape]
      self.delete(shape, group)

   def delete_group(self, group):
      for shape in self.groups[group]:
         self.delete(shape)
      del self.groups[group]
      
   def has(self, shape):
      """
      :param shape: Shape to check for
      :type shape: Shape
      :return: True if the space contains the shape, False if not
      :rtype: bool

      Checks if a space has a shape in that shape's area
      Note that the shape's must be set correctly or errors can occur
      """
      return shape in self.ids

   def has_id(self, id):
      return id in self.shapes

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
      collisions = []
      for other in self.grid.get(self.grid.scale(x, y)):
         if self.collidable[shape]:
            if self.collider.rect_rect(width, height, x, y, other.width, other.height, other.position[0], other.position[1]):
               collisions.append(other)
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
      id = self.ids[shape]
      for other in self.grid.get(self.areas[shape]):
         if self.collidable[shape]:
            if id != self.ids[other]:
               if self.collider.rect_rect(shape.width, shape.height, shape.position[0], shape.position[1], other.width, other.height, other.position[0], other.position[1]):
                  collisions.append(other)
      return collisions

   def collisions_with_group(self, group):
      collisions = []
      group = self.groups[group]
      for shape in group:
         if self.collidable[shape]:
            id = self.ids[shape]
            for other in self.grid.get(self.areas[shape]):
               if self.collidable[shape]:
                  if id != self.ids[other]:
                     if other not in group:
                        if self.collider.rect_rect(shape.width, shape.height, shape.position[0], shape.position[1], other.width, other.height, other.position[0], other.position[1]):
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
      for other in self.grid.get(self.grid.scale(x, y)):
         if self.collidable[other]:
            if self.collider.rect_rect(width, height, x, y, other.width, other.height, other.position[0], other.position[1]):
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
      id = self.ids[shape]
      for other in self.grid.get(self.areas[shape]):
         if self.collidable[other]:
            if id != self.ids[other]:
               if self.collider.rect_rect(shape.width, shape.height, shape.position[0], shape.position[1], other.width, other.height, other.position[0], other.position[1]):
                  return True
      return False

   def check_group(self, group):
      group = self.groups[group]
      for shape in group:
         if self.collidable[shape]:
            id = self.ids[shape]
            for other in self.grid.get(self.areas[shape]):
               if self.collidable[other]:
                  if id != self.ids[other]:
                     if other not in group:
                        if self.collider.rect_rect(shape.width, shape.height, shape.position[0], shape.position[1], other.width, other.height, other.position[0], other.position[1]):
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
      start = self.areas[shape]
      if start != area:
         self.move_area(shape, area)
         return start
      else:
         return None

   def move_area(self, shape, area):
      #TODO this needs to be optimized better but I'm not doing it right now
      start = self.areas[shape]
      self.delete_from_grid(shape, area)
      self.add_to_grid(shape, area)
      self.areas[shape] = area

   def delete_from_grid(self, shape, area):
      self.grid.delete(shape, area)
      self.grid.delete(shape, (area[0]+1, area[1]))
      self.grid.delete(shape, (area[0], area[1]+1))
      self.grid.delete(shape, (area[0]+1, area[1]+1))

   def add_to_grid(self, shape, area):
      self.grid.add(shape, area)
      self.grid.add(shape, (area[0]+1, area[1]))
      self.grid.add(shape, (area[0], area[1]+1))
      self.grid.add(shape, (area[0]+1, area[1]+1))
      
   def move(self, shape, distance):
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
      
      Advances a shape in its direction for distance units.
      """
      direction = self.directions[shape]
      xstep = int(direction[0] * distance)
      ystep = int(direction[1] * distance)
      shape.position = (shape.position[0]+xstep, shape.position[1]+ystep)
      self.update_area(shape)
      return (xstep, ystep)

   def move_group(self, group, distance):
      #TODO this could be optimized in some/most cases by uniform group movement to not recalc the direction a shape moves for every shape.
      for shape in self.groups[group]:
         self.move(shape, distance)

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
      self.update_area(shape)

   def push_group(self, group, x, y):
      for shape in self.groups[group]:
         self.push(shape, x, y)

   def place(self, shape, x, y):
      """
      :param x: The position in space to place the shape on the horizontal plane
      :param y: The position in space to place the shape on the vertical plane
      :type x: int
      :type y: int

      Directly places a shape at x, y in space
      """
      shape.position = (x, y)
      self.update_area(shape)

   def place_group(self, group, x, y):
      for shape in self.groups[group]:
         self.place(shape, x, y)

   def set_moving(self, shape, value):
      self.moving[shape] = value

   def set_moving_group(self, group, value):
      for shape in self.groups[group]:
         self.moving[shape] = value

   def set_collidable(self, shape, value):
      self.collidable[shape] = value

   def set_collidable_group(self, group, value):
      for shape in self.groups[group]:
         self.collidable[shape]= value
         
   def turn(self, shape, direction):
      self.directions[shape] = direction

   def turn_group(self, group, direction):
      for shape in self.groups[group]:
         self.directions[shape] = direction


   def step(self, delta):
      """
      :param delta: Units of time to advance the simulation
      :type delta: float
      Process the system for delta steps.
      Triggers the on_step_start(delta), on_step(body, delta), on_collision(body, collisions), and on_step_end(delta) callbacks
      """
      self.on_step_start(delta)
      for shape in self.actives:
         self.on_step(shape, delta)
         if self.moving[shape]:
            self.move(shape, delta)

      #TODO This is very unoptimized
      for shape in self.actives:
         collisions = self.collisions_with(shape)
         if collisions:
            self.on_collision(shape, collisions)
      self.on_step_end(delta)

   def on_step_start(self, delta):
      """
      :param delta: Units of time to advance the simulation
      :type delta: float
      Callback before the simulation takes a step. Override this when extending your Controller
      """
      return


   def on_step(self, shape, delta):
      """
      :param body: Body being processed by the step
      :param delta: Units of time to advance the simulation
      :type body: Body
      :type delta: float
      Callback when the simulation takes a step over a body. Override this when extending your Controller
      """
      return

   def on_collision(self, shape, collisions):
      """
      :param body: Body involved in a collision
      :param collision: List of bodies colliding with body
      :type body: Body
      :type other: List(Body)
      Callback when bodies collide with another body. Override this when extending your Controller
      """
      return

   def on_step_end(self, delta):
      """
      :param delta: Units of time to advance the simulation
      :type delta: float
      Callback after the simulation takes a step. Override this when extending your Controller
      """
      return
      
