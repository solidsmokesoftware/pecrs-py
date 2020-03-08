import pecrs
from pecrs import *


def test_body():
  passing = True

  rectA = Rect(0, 0, 32, 32)
  rectB = Rect(0, 0, 32, 32)
  circle = Circle(0, 0, 64)

  absbody = AbsBody(0, circle)
  body = Body(1, rectA)
  body.direction = (1, 0)
  body.speed = 100

  staticbody = StaticBody(2, rectB)

  body.move(10)
  expected = (1000, 0)
  print(f"Body test: move({10}) expecting {expected}, actual {str(body.shape.position)}")
  if body.shape.position != expected:
    print("Fail")
    passing = False

  body.move_to(-1, 0, 5)
  expected = (500, 0)
  print(f"Body test: move_to(-1, 0, 5) expecting {expected}, actual {str(body.shape.position)}")
  if body.shape.position != expected:
    print("Fail")
    passing = False

  staticbody.place(0, 250)
  expected = (0, 250)
  print(f"Body test: place(0, 250) expecting {expected}, actual {str(staticbody.shape.position)}")
  if staticbody.shape.position != expected:
    print("Fail")
    passing = False

  if passing:
    print("Body test: Complete, all tests passed")
  else:
    print("Body test: Incomplete, some tests failed")
  return passing


def test_index():
  passing = True

  index = Index()

  a = index.next()
  print(f"Index test: next() expecting 0, actual {a}")
  if a != 0:
    print("Fail")
    passing = False

  b = index.next()
  print(f"Index test: next() expecting 1, actual {b}")
  if b != 1:
    print("Fail")
    passing = False

  print(f"Index test: add({a}, {a})")
  index.add(a, a)

  print(f"Index test: add({b}, {b})")
  index.add(b, b)

  print(f"Index test: add({2})")
  index.add(2)

  index.delete(a)
  print(f"Index test: delete({a})")

  d = index.next()
  print(f"Index test: next() expecting 0, actual {d}")
  if d != 0:
    print("Fail")
    passing = False

  index.delete(b)
  print(f"Index test: delete({b})")

  e = index.next()
  print(f"Index test: next() expecting 1, actual {e}")
  if e != 1:
    print("Fail")
    passing = False

  f = index.next()
  print(f"Index test: next() expecting 3, actual {f}")
  if f != 3:
    print("Fail")
    passing = False

  g = index.next()
  print(f"Index test: next() expecting 4, actual {g}")
  if g != 4:
    print("Fail")
    passing = False

  if passing:
    print("Index test: Complete, all tests passed")
  else:
    print("Index test: Incomplete, some tests failed")
  return passing

def test_collider():
  passing = True

  collider = Collider()
  rectA = Rect(0, 0, 10, 10)
  rectB = Rect(0, 0, 10, 10)
  circleA = Circle(0, 0, 10)
  circleB = Circle(0, 0, 10)

  collider.check_shapes(rectA, rectB)
  print(f"Collider test: check(Rect, Rect)")

  collider.check_shapes(rectA, circleA)
  print(f"Collider test: check(Rect, Circle)")

  collider.check_shapes(circleB, rectB)
  print(f"Collider test: check(Circle, Rect)")

  collider.check_shapes(circleA, circleB)
  print(f"Collider test: check(Circle, Circle)")

  rectA.position = 0, 0
  rectB.position = 0, 9
  value = collider.check_rects(rectA, rectB)
  print(f"Collision test: check_rect({str(rectA.position)}, {str(rectB.position)}) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  rectA.position = 0, 0
  rectB.position = 5, -5
  value = collider.rect_rect(rectA.width, rectA.height, rectA.position[0], rectA.position[1], rectB.width, rectB.height, rectB.position[0], rectB.position[1])
  print(f"Collision test: rect_rect(...) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  rectA.position = 0, 0
  rectB.position = 9, 9
  value = collider.check_rects(rectA, rectB)
  print(f"Collision test: checks_rect({str(rectA.position)}, {str(rectB.position)}) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  rectA.position = 0,0
  rectB.position = 0, 10
  value = collider.rect_rect(rectA.width, rectA.height, rectA.position[0], rectA.position[1], rectB.width, rectB.height, rectB.position[0], rectB.position[1])
  print(f"Collision test: rect_rect(...) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  rectA.position = 0,0
  rectB.position = 10, 0
  value = collider.check_rects(rectA, rectB)
  print(f"Collision test: check_rects({str(rectA.position)}, {str(rectB.position)}) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  rectA.position = 0,0
  circleB.position = 10, 0
  value = collider.rect_circle(rectA.width, rectA.height, rectA.position[0], rectA.position[1], circleB.radius, circleB.position[0], circleB.position[1])
  print(f"Collision test: rect_circle({str(rectA.position)}, {str(circleB.position)}) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False
  
  rectA.position = 0,0
  circleB.position = 20, 0
  value = collider.rect_circle(rectA.width, rectA.height, rectA.position[0], rectA.position[1], circleB.radius, circleB.position[0], circleB.position[1])
  print(f"Collision test: rect_circle({str(rectA.position)}, {str(circleB.position)}) expecting True, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  circleA.position = 0, 0
  rectB.position = -5, 0
  value = collider.circle_rect(circleA.radius, circleA.position[0], circleA.position[1], rectB.width, rectB.height, rectB.position[0], rectB.position[1])
  print(f"Collision test: circle_rect({str(circleA.position)}, {str(rectB.position)}) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False
  
  circleA.position = 0, 0
  rectB.position = 19, 2
  value = collider.circle_rect(circleA.radius, circleA.position[0], circleA.position[1], rectB.width, rectB.height, rectB.position[0], rectB.position[1])
  print(f"Collision test: circle_rect({str(circleA.position)}, {str(rectB.position)}) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  circleA.position = 0, 0
  circleB.position = -5, 0  
  value = collider.check_circles(circleA, circleB)
  print(f"Collision test: check_circles(circleA, circleB) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  circleA.position = 0, 0
  circleB.position = 19, 0
  value = collider.circle_circle(circleA.radius, circleA.position[0], circleA.position[1], circleB.radius, circleB.position[0], circleB.position[1])
  print(f"Collision test: circle_circle(...) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  circleA.position = 0, 0
  circleB.position = 20, 0
  value = collider.circle_circle(circleA.radius, circleA.position[0], circleA.position[1], circleB.radius, circleB.position[0], circleB.position[1])
  print(f"Collision test: circle_circle(...) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  circleA.position = 0, 0
  circleB.position = 14, 14  
  value = collider.check_circles(circleA, circleB)
  print(f"Collision test: check_circles(circleA, circleB) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  circleA.position = 0, 0
  circleB.position = 15, 15
  value = collider.circle_circle(circleA.radius, circleA.position[0], circleA.position[1], circleB.radius, circleB.position[0], circleB.position[1])
  print(f"Collision test: circle_circle(...) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False
  
  if passing:
    print("Collider test: Complete, all tests passed")
  else:
    print("Collider test: Incomplete, some tests failed")
  return passing


def test_spatialhash():
  passing = True
  spatialhash = SpatialHash(10)

  value = spatialhash.scale(5, 5)
  print(f"SpatialHash test: scale(5, 5) expecting (0, 0), actual {value}")
  if value != (0, 0):
    print("Fail")
    passing = False

  value = spatialhash.scale(9, 5)
  print(f"SpatialHash test: scale(9, 5) expecting (0, 0), actual {value}")
  if value != (0, 0):
    print("Fail")
    passing = False

  value = spatialhash.scale(10, 0)
  print(f"SpatialHash test: scale(10, 0) expecting (1, 0), actual {value}")
  if value != (1, 0):
    print("Fail")
    passing = False

  value = spatialhash.scale(11, 0)
  print(f"SpatialHash test: scale(11, 0) expecting (1, 0), actual {value}")
  if value != (1, 0):
    print("Fail")
    passing = False

  value = spatialhash.scale(20, 10)
  print(f"SpatialHash test: scale(20, 10) expecting (2, 1), actual {value}")
  if value != (2, 1):
    print("Fail")
    passing = False

  spatialhash.add_pos(1, 0, 0)
  spatialhash.add_pos(2, 0, 0)
  spatialhash.add(3, (0, 0))
  spatialhash.add(4, (1, 0))
  spatialhash.add(5, (1, 0))

  value = spatialhash.has(1)
  print(f"SpatialHash test: has(1) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  value = spatialhash.has(10)
  print(f"SpatialHash test: has(10) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  value = spatialhash.has(1, (1, 1))
  print(f"SpatialHash test: has(1, (1, 1)) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  value = spatialhash.has(1, (1, 0))
  print(f"SpatialHash test: has(1, (1, 0)) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  value = spatialhash.has(1, (0, 0))
  print(f"SpatialHash test: has(1, (0, 0)) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  value = spatialhash.get((0, 0))
  print(f"SpatialHash test: get(0, 0) expecting [1, 2, 3], actual {value}")
  if value != [1, 2, 3]:
    print("Fail")
    passing = False

  value = spatialhash.get((1, 0))
  print(f"SpatialHash test: get(1, 0) expecting [4, 5], actual {value}")
  if value != [4, 5]:
    print("Fail")
    passing = False

  value = spatialhash.get_pos(0, 0)
  print(f"SpatialHash test: get_pos(0, 0) expecting [1, 2, 3], actual {value}")
  if value != [1, 2, 3]:
    print("Fail")
    passing = False

  value = spatialhash.get_pos(15, 0)
  print(f"SpatialHash test: get_pos(15, 0) expecting [4, 5], actual {value}")
  if value != [4, 5]:
    print("Fail")
    passing = False

  spatialhash.delete(3, (1, 0))
  value = spatialhash.get((1, 0))
  print(f"SpatialHash test: delete(3, (1, 0)) expecting [4, 5], actual {value}")
  if value != [4, 5]:
    print("Fail")
    passing = False

  spatialhash.delete(3, (0, 0))
  value = spatialhash.get((0, 0))
  print(f"SpatialHash test: delete(3, (0, 0)) expecting [1, 2], actual {value}")
  if value != [1, 2]:
    print("Fail")
    passing = False
  
  spatialhash.delete_pos(1, 0, 0)
  value = spatialhash.get_pos(0, 0)
  print(f"SpatialHash test: delete(1, (0, 0)) expecting [2], actual {value}")
  if value != [2]:
    print("Fail")
    passing = False

  if passing:
    print("Collider test: Complete, all tests passed")
  else:
    print("Collider test: Incomplete, some tests failed")
  return passing


def test_space():
  passing = True

  space = Space(128)

  rectA = Rect(0, 0, 32, 32)
  rectB = Rect(0, 0, 32, 32)
  rectC = Rect(0, 64, 32, 32)
  rectD = Rect(0, 256, 32, 32)
  bodyA = Body(0, rectA)
  bodyB = Body(1, rectB)
  bodyC = Body(2, rectC)
  bodyD = Body(3, rectD)


  value = space.has(bodyA)
  print(f"Space test: has(bodyA)) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  space.add(bodyA)
  print("Space test: add(BodyA)")
  space.add(bodyB, (0, 0))
  print("Space test: add(BodyB, (0, 0))")
  space.add(bodyC)
  print("Space test: add(BodyC)")
  space.add(bodyD)
  print("Space test: add(BodyD)")

  value = space.has(bodyA)
  print(f"Space test: has(bodyA)) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  value = space.has(bodyA)
  print(f"Space test: has(bodyB)) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  value = space.collisions_at(0, 0, 32, 32)
  print(f"Space test: collisions_at(0, 0, 32, 32) expecting [...], actual [...]")
  for v in value:
    if v.id == bodyA.id or v.id == bodyB.id:
      pass
    else:
      print(f"Fail {v.id}")
      passing = False

  value = space.collisions_at(0, 64)
  print(f"Space test: colliding_at(0, 64) expecting [...], actual [...]")
  for v in value:
    if v.id != bodyC.id:
      print("Fail")
      passing = False

  value = space.collisions_with(bodyA)
  print(f"Space test: collisions_with(bodyA) expecting [...], actual [...]")
  for v in value:
    if v.id != bodyB.id:
      print("Fail")
      passing = False

  value = space.collisions_with(bodyD)
  print(f"Space test: collisions_with(bodyD) expecting [...], actual [...]")
  if value != []:
    print("Fail")
    passing = False

  value = space.check_bodies(bodyA, bodyB)
  print(f"Space test: check_bodies(bodyA, bodyB) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  value = space.check_bodies(bodyC, bodyD)
  print(f"Space test: check_bodies(bodyC, bodyD) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  value = space.check_body(bodyA)
  print(f"Space test: check_body(bodyA) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  value = space.check_body(bodyC)
  print(f"Space test: check_body(bodyC) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  bodyD.place(0, 0)
  space.place(bodyD, (0, 0))
  print("Space test: place(bodyD, (0, 0))")

  value = space.collisions_with(bodyA)
  print(f"Space test: collisions_with(bodyA) expecting [...], actual [...]")
  for v in value:
    if v.id == bodyB.id or v.id == bodyD.id:
      pass
    else:
      print("Fail")
      passing = False

  space.delete(bodyA)
  print("Space test: delete(bodyA)")

  value = space.collisions_with(bodyB)
  print(f"Space test: collisions_with(bodyB) expecting [...], actual [...]")
  for v in value:
    if v.id != bodyD.id:
      print("Fail")
      passing = False

  if passing:
    print("Space test: Complete, all tests passed")
  else:
    print("Space test: Incomplete, some tests failed")
  return passing


def test_controller():
  passing = True

  #TODO test controller.remake_space()

  class Entity(Body):
    def __init__(self, id, shape):
      super().__init__(id, shape)

  class Objects(Controller):
    def __init__(self):
      super().__init__()

    def on_add(self, body):
      print(f"on_add callback {body.id}")

    def on_make(self, body):
      body.speed = 100
      body.moving = True
      print(f"on_make callback {body.id}")

    def on_delete(self, body):
      print(f"on_delete callback {body.id}")

    def on_area(self, body, start):
      print(f"on_area callback {body.id} from {start} to {body.area}")

    def on_move(self, body, distance):
      print(f"on_move callback {body.id} moved {distance} units")

    def on_place(self, body, start):
      print(f"on_place callback {body.id} moved from {start}")

    def on_motion(self, body):
      print(f"body {body.id} at {str(body.shape.position)}")

    def on_turn(self, body):
      print(f"on_turn callback {body.id} to {str(body.direction)}")

    def on_start(self, body):
      print(f"on_start callback {body.id}")

    def on_stop(self, body):
      print(f"on_stop callback {body.id}")

    def on_step_start(self, delta):
      print("on_step_start callback")

    def on_step(self, body, delta):
      print(f"on_step callback {body.id} {delta}")

    def on_step_end(self, delta):
      print("on_step_end callback")

  objects = Objects()

  bodyA = objects.make(Entity, 0, 0, 32, 32)
  print(f"Controller test: make(Entity, 0, 0, 32, 32) expecting id 0, actual {bodyA.id}")
  if bodyA.id != 0:
    print("Fail")
    passing = False

  bodyB = objects.make(Entity, 0, 0, 32, 32, dx=1)
  print(f"Controller test: make(Entity, 0, 0, 32, 32, dx=1) expecting id 1, actual {bodyB.id}")
  if bodyB.id != 1:
    print("Fail")
    passing = False

  bodyC = objects.make(Entity, 0, 0, 32, 32, dy=1)
  print(f"Controller test: make(Entity, 0, 0, 32, 32 dy=1) expecting id 2, actual {bodyC.id}")
  if bodyC.id != 2:
    print("Fail")
    passing = False

  bodyD = objects.make(Entity, 0, 0, 32, 32)
  print(f"Controller test: make(Entity, 0, 0, 32, 32) expecting id 3, actual {bodyD.id}")
  if bodyD.id != 3:
    print("Fail")
    passing = False

  objects.move(bodyA, 1)
  objects.move(bodyB, 1)
  objects.move_to(bodyD, 0, 1, 1)
  objects.place(bodyC, 10, 10)

  objects.turn(bodyD, -1, 0)

  objects.step(1)

  objects.delete(bodyA)
  objects.delete_id(bodyD.id)

  objects.step(1)

  if passing:
    print("Space test: Complete, all tests passed")
  else:
    print("Space test: Incomplete, some tests failed")
  return passing

def test():
  passing = True
  if not test_body():
    passing = False
  
  if not test_index():
    passing = False

  if not test_collider():
    passing = False

  if not test_spatialhash():
    passing = False

  if not test_space():
    passing = False

  if not test_controller():
    passing = False

  if passing:
    print(f"pecrs version {pecrs.version} test: Complete, all tests passed")
  else:
    print(f"pecrs version {pecrs.version} test: Incomplete, some tests failed")

test()

clock = Clock(100) 
sync_clock = SyncClock()