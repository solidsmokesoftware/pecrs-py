
from pecrs.index import Index
from pecrs.space import Space
from pecrs.body import *
from pecrs.shape import *


class Controller:
   """
   :param size: Size of each collision area, in pixels. A large area means less area changes while moving but more collision checks
   :type size: int

   High-level manager of the physics system.
   """
   def __init__(self, size=256):
      self.index = Index() #: Index, Indexing system used to track bodies.
      self.actives = [] #: list, stores Body for processing.
      self.space = Space(size) #: Space partionining system.

   def remake_space(self, size):
      """
      :param size: Size of the new Space
      :type size: int

      Makes a new Space and fills it with all the bodies in the Index.
      """
      self.space = Space(size)
      for id in self.index.list:
         self.space.add(self.index.list[id].shape)

   def make_from(self, kind, shape, id=None, dx=0, dy=0):
      """
      :param kind: Class to be created
      :param shape: Shape of the new body
      :param id: Unique identifer to assign to the body, generated by Index if None
      :param dx: Directional facing of the body
      :param dy: Directional facing of the body
      :type kind: Uninstanced AbsBody
      :type shape: Shape
      :type id: int
      :type dx: int
      :type dy: int
      :return: Newly created body
      :rtype: kind

      Produces a body of `kind` from `shape` and adds it to the system
      Triggers `on_make(body)` and `on_add(body)` callbacks
      """
      if not id:
         id = self.index.next()
      body = kind(id, shape)
      body.direction = (dx, dy)
      self.on_make(body)
      self.add(body)
      return body

   def make(self, kind, x, y, width, height, id=None, dx=0, dy=0):
      """
      :param kind: Class to be created
      :param x: Position in space to create the body on the horizontal plane
      :param y: Position in space to create the body on the vertical plane
      :param width: Width of the new body
      :param height: Height of the new body
      :param id: Unique identifer to assign to the body, generated by Index if None
      :param dx: Directional facing of the body
      :param dy: Directional facing of the body
      :type kind: Uninstanced AbsBody
      :type x: int
      :type y: int
      :type width: int
      :type height: int
      :type id: int
      :type dx: int
      :type dy: int
      :return: Newly created body
      :rtype: kind

      Creates a Rect at position `x`, `y` with a `height` and `width`, then makes a body with it using `Controller.make_with()`
      """
      shape = Rect(x, y, width, height)
      return self.make_from(kind, shape, id, dx, dy)

   def on_make(self, body):
      """
      :param body: Body that was made by the system
      :type body: AbsBody
      
      Callback when bodies are made by the system. Override this when extending your Controller
      """
      return

   def add(self, body):
      """
      :param body: Body to be added to the system
      :type body: AbsBody

      Adds a body to the system and space.

      Triggers on_add(body) callback
      """
      self.index.add(body, body.id)
      self.space.add(body.shape)
      if isinstance(body, Body): #TODO there might be a better way to do this?
         self.actives.append(body)

      self.on_add(body)

   def on_add(self, body):
      """
      :param body: Body that was added to the system
      :type body: AbsBody

      Callback when bodies are added to the system. Override this when extending your Controller
      """
      return

   def delete(self, body):
      """
      :param body: Body to be removed from the system
      :type body: AbsBody

      Removes a body from the system.
      Triggers on_delete(body) callback
      """
      self.index.delete(body.id)
      self.space.delete(body.shape)
      if isinstance(body, Body):
         self.actives.remove(body)
      self.on_delete(body)

   def delete_id(self, id):
      """
      :param id: id of the body to be removed from the system
      :type id: int

      Removes a body from the system by id.
      Triggers on_delete(body) callback
      """
      body = self.index.list[id]
      self.delete(body)

   def on_delete(self, body):
      """
      :param body: Body removed from the system
      :type body: AbsBody

      Callback when bodies are deleted by the system. Override this when extending your Controller
      """
      return

   def move(self, body, delta):
      """
      :param body: Body to be moved by the system
      :param delta: Units of time to move the body
      :type body: AbsBody
      :type delta: float

      Move a body by it's speed and direction for delta.
      Triggers the on_move(body, distance) and on_motion(body) callbacks
      """
      return self.move_to(body, body.direction[0], body.direction[1], delta)

   def move_to(self, body, x, y, delta):
      """
      :param body: Body to be moved by the system
      :param x: Direction to move the body in on the horitzontal plane
      :param y: Direction to move the body in on the vertical plane
      :param delta: Units of time to advance the simulation by
      :type body: AbsBody
      :type x: int
      :type y: int
      :type delta: float

      Move a body by it's speed in the direction of x, y for delta.
      Triggers the on_move(body, distance) and on_motion(body) callbacks
      """
      distance = self.space.move(body.shape, x, y, body.speed*delta)
      self.on_move(body, distance)
      self.on_motion(body)
      return distance

   def on_move(self, body, distance):
      """
      :param body: Body that was moved by the system
      :param distance: The distance moved by the body
      :type body: AbsBody
      :type distance: tuple(int, int)

      Callback when bodies are moved by the system. Override this when extending your Controller
      """
      return

   def push(self, body, x, y):
      """
      :param body: Body to be pushed by the system
      :param x: Direction to push the body in on the horitzontal plane
      :param y: Direction to push the body in on the vertical plane
      :type body: AbsBody
      :type x: int
      :type y: int

      Pushes a body in the direction of x, y.
      Triggers callbacks for on_push(body, x, y) and on_motion(body)
      """
      self.space.push(body.shape, x, y)
      self.on_push(body, x, y)
      self.on_motion(body)

   def on_push(self, body, x, y):
      """
      :param body: Body that was pushed in space by the system
      :param x: Direction the body was pushed in on the horitzontal plane
      :param y: Direction the body was pushed in on the vertical plane
      :type body: AbsBody
      :type x: int
      :type y: int

      Callback when bodies are pushed by the system. Override this when extending your Controller
      """
      return

   def place(self, body, x, y):
      """
      :param body: Body to be placed in space by the system
      :param x: Position to place the body in on horitzontal plane
      :param y: Position to place the body in on the vertical plane
      :type body: AbsBody
      :type x: int
      :type y: int

      Directly place a body at x, y
      Triggers the callbacks on_place(body, start) and on_motion(body)
      Use this instead of body.place(x, y) to keep track of collision area
      """
      start = body.shape.position
      self.space.place(body, x, y)
      self.on_place(body, start)
      self.on_motion(body)

   def on_place(self, body, start):
      """
      :param body: Body that was placed by the system
      :param start: The location of the body before being placed
      :type body: AbsBody
      :type start: Tuple(Int, Int)

      Callback triggered when bodies are placed by the system. Override this when extending your Controller
      """
      return

   def on_motion(self, body):
      """
      :param body: Body that had its position changed by the system.
      :type body: AbsBody

      Callback when bodies change positions. This is triggered by both move and place. Override this when extending your Controller
      """
      return

   def turn(self, body, x, y):
      """
      :param body: Body to be rotated from the system
      :param x: Direction to move to in the horitzontal plane
      :param y: Direction to move to in the vertical plane
      :type body: AbsBody()
      :type x: int
      :type y: int

      Change the direction of a body
      """
      body.direction = (x, y)
      self.on_turn(body)

   def on_turn(self, body):
      """
      :param body: Body that was turned
      :type body: AbsBody()

      Callback when a body is turned by the system. Override this when extending your Controller
      """
      return

   def start(self, body):
      """
      :param body: Body to active for movement during processing by the system
      :type body: AbsBody()

      Tells a body to move when the system is processed.
      """
      body.moving = True
      self.on_start(body)

   def on_start(self, body):
      """
      :param body: Body that was actived for movement
      :type body: AbsBody()

      Callback when bodies are told to move by the system. Override this when extending your Controller
      """
      return

   def stop(self, body):
      """
      :param body: Body to deactived system movement processing for
      :type body: AbsBody()

      Tells a body to not move when the system is proccessed.
      """
      body.moving = False
      self.on_stop(body)

   def on_stop(self, body):
      """
      :param body: Body that was deactived for movement
      :type body: AbsBody()
      
      Callback when bodies are told to stop by the system. Override this when extending your Controller
      """
      return 
      
   def get(self, id):
      """
      :param id: id of the body to get
      :type id: int
      :return: AbsBody or None
      :rtype: AbsBody or None

      Gets an body by its id.
      """
      if id in self.index.list:
         return self.index.list[id]
      else:
         return None
         
   def collisions_at(self, x, y, width=1, height=1):
      """
      :param x: Position to seach for on in the horitzontal plane
      :param y: Position to seach for on in the vertical plane
      :type x: int
      :type y: int
      :return: A list of bodies located at x, y
      :rtype: List(AbsBody)

      Finds all of the bodies at x, y.
      """
      return self.space.collisions_at(x, y, width, height)

   def collisions_with(self, body):
      """
      :param body: Body to check for collisions
      :type body: AbsBody
      :return: A list of bodies colliding with body
      :rtype: List(AbsBody)

      Finds all bodies colliding with body.
      """
      return self.space.collisions_with(body.shape)

   def check(self, body):
      """
      :param body: Body to check for collisions with
      :type body: AbsBody
      :return: True if Collisions, False is not
      :rtype: Bool

      Check to see if any shapes are colliding with the Body in space
      """
      return self.space.check(body.shape)

   def check_two(self, body, other):
      """
      :param body: First Body to check for collision
      :param other: Second Body to check for collision 
      :type body: AbsBody
      :type other: AbsBody
      :return: True if the two bodies are colliding, False is not
      :rtype: Bool

      Check to see if the two bodies are colliding.
      """
      return self.space.check_two(body.shape, other.shape)

   def step(self, delta):
      """
      :param delta: Units of time to advance the simulation
      :type delta: float

      Process the system for delta steps.
      Triggers the on_step_start(delta), on_step(body, delta), on_collision(body, collisions), and on_step_end(delta) callbacks
      """
      self.on_step_start(delta)
      for body in self.actives:
         self.on_step(body, delta)
         if body.moving:
            self.move(body, delta)

      #TODO This is very unoptimized
      for body in self.actives:
         collisions = self.space.collisions_with(body.shape)
         if collisions:
            self.on_collision(body, collisions)
      self.on_step_end(delta)

   def on_step_start(self, delta):
      """
      :param delta: Units of time to advance the simulation
      :type delta: float

      Callback before the simulation takes a step. Override this when extending your Controller
      """
      return


   def on_step(self, body, delta):
      """
      :param body: Body being processed by the step
      :param delta: Units of time to advance the simulation
      :type body: AbsBody
      :type delta: float

      Callback when the simulation takes a step over a body. Override this when extending your Controller
      """
      return

   def on_collision(self, body, collisions):
      """
      :param body: Body involved in a collision
      :param collision: List of bodies colliding with body
      :type body: AbsBody
      :type other: List(AbsBody)

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
      

         