
from pecrs import *


def test_body():
  passing = True

  vectorA = Vector(0, 0)
  vectorB = Vector(0, 0)
  expected = Vector(0, 0)
  rect = Rect(32, 32)
  circle = Circle(64)

  absbody = AbsBody(0, vectorA, circle)
  body = Body(1, vectorA, rect)
  body.direction.x = 1
  body.speed = 100
  staticbody = StaticBody(2, vectorA, rect)

  body.move(10)
  print(f"Body test: move({10}) expecting 1000:0, actual {str(body.position)}")
  expected.x = 1000
  if body.position != expected:
    print("Fail")
    passing = False

  body.move_to(-1, 0, 5)
  print(f"Body test: move_to(-1, 0, 5) expecting 500:0, actual {str(body.position)}")
  expected.x = 500
  if body.position != expected:
    print("Fail")
    passing = False

  staticbody.place(0, 250)
  print(f"Body test: place(0, 250) expecting 0:250, actual {str(body.position)}")
  expected.x = 0
  expected.y = 250
  if body.position != expected:
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

  a = index.get()
  print(f"Index test: get() expecting 0, actual {a}")
  if a != 0:
    print("Fail")
    passing = False

  b = index.get()
  print(f"Index test: get() expecting 1, actual {b}")
  if b != 1:
    print("Fail")
    passing = False

  c = index.get()
  print(f"Index test: get() expecting 2, actual {c}")
  if c != 2:
    print("Fail")
    passing = False

  index.delete(a)
  print(f"Index test: delete({a})")

  d = index.get()
  print(f"Index test: get() expecting 0, actual {d}")
  if d != 0:
    print("Fail")
    passing = False

  index.delete(b)
  print(f"Index test: delete({b})")

  index.delete(c)
  print(f"Index test: delete({c})")

  e = index.get()
  print(f"Index test: get() expecting 2, actual {e}")
  if e != 2:
    print("Fail")
    passing = False

  f = index.get()
  print(f"Index test: get() expecting 1, actual {f}")
  if f != 1:
    print("Fail")
    passing = False

  g = index.get()
  print(f"Index test: get() expecting 3, actual {g}")
  if g != 3:
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
  rectA = Rect(10, 10)
  rectB = Rect(10, 10)
  circleA = Circle(10)
  circleB = Circle(10)
  positionA = Vector(0, 0)
  positionB = Vector(0, 0)

  collider.check(rectA, positionA, rectB, positionB)
  print(f"Collider test: check(Rect, Rect)")

  collider.check(rectA, positionA, circleA, positionB)
  print(f"Collider test: check(Rect, Circle)")

  collider.check(circleB, positionA, rectB, positionB)
  print(f"Collider test: check(Circle, Rect)")

  collider.check(circleA, positionA, circleB, positionB)
  print(f"Collider test: check(Circle, Circle)")

  positionA.x = 0
  positionA.y = 0
  positionB.x = 0
  positionB.y = 9
  value = collider.rect_rect(rectA, positionA, rectB, positionB)
  print(f"Collision test: rect_rect({str(positionA)}, {str(positionB)}) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  positionA.x = 0
  positionA.y = 0
  positionB.x = 5
  positionB.y = -5
  value = collider.rect_rect(rectA, positionA, rectB, positionB)
  print(f"Collision test: rect_rect({str(positionA)}, {str(positionB)}) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  positionA.x = 0
  positionA.y = 0
  positionB.x = 9
  positionB.y = 9
  value = collider.rect_rect(rectA, positionA, rectB, positionB)
  print(f"Collision test: rect_rect({str(positionA)}, {str(positionB)}) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  positionA.x = 0
  positionA.y = 0
  positionB.x = 0
  positionB.y = 10
  value = collider.rect_rect(rectA, positionA, rectB, positionB)
  print(f"Collision test: rect_rect({str(positionA)}, {str(positionB)}) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  positionA.x = 0
  positionA.y = 0
  positionB.x = 10
  positionB.y = 0
  value = collider.rect_rect(rectA, positionA, rectB, positionB)
  print(f"Collision test: rect_rect({str(positionA)}, {str(positionB)}) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  positionA.x = 0
  positionA.y = 0
  positionB.x = 10
  positionB.y = 0
  value = collider.rect_circle(rectA, positionA, circleB, positionB)
  print(f"Collision test: rect_circle({str(positionA)}, {str(positionB)}) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False
  
  positionA.x = 0
  positionA.y = 0
  positionB.x = 20
  positionB.y = 0
  value = collider.rect_circle(rectA, positionA, circleB, positionB)
  print(f"Collision test: rect_circle({str(positionA)}, {str(positionB)}) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  positionA.x = 0
  positionA.y = 0
  positionB.x = -5
  positionB.y = 0
  value = collider.circle_rect(circleA, positionA, rectB, positionB)
  print(f"Collision test: circle_rect({str(positionA)}, {str(positionB)}) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False
  
  positionA.x = 0
  positionA.y = 0
  positionB.x = 19
  positionB.y = 2 
  value = collider.circle_rect(circleA, positionA, rectB, positionB)
  print(f"Collision test: circle_rect({str(positionA)}, {str(positionB)}) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  positionA.x = 0
  positionA.y = 0
  positionB.x = -5
  positionB.y = 0  
  value = collider.circle_circle(circleA, positionA, circleB, positionB)
  print(f"Collision test: circle_circle({str(positionA)}, {str(positionB)}) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  positionA.x = 0
  positionA.y = 0
  positionB.x = 19
  positionB.y = 0  
  value = collider.circle_circle(circleA, positionA, circleB, positionB)
  print(f"Collision test: circle_circle({str(positionA)}, {str(positionB)}) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  positionA.x = 0
  positionA.y = 0
  positionB.x = 20
  positionB.y = 0  
  value = collider.circle_circle(circleA, positionA, circleB, positionB)
  print(f"Collision test: circle_circle({str(positionA)}, {str(positionB)}) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  positionA.x = 0
  positionA.y = 0
  positionB.x = 14
  positionB.y = 14  
  value = collider.circle_circle(circleA, positionA, circleB, positionB)
  print(f"Collision test: circle_circle({str(positionA)}, {str(positionB)}) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  positionA.x = 0
  positionA.y = 0
  positionB.x = 15
  positionB.y = 15  
  value = collider.circle_circle(circleA, positionA, circleB, positionB)
  print(f"Collision test: circle_circle({str(positionA)}, {str(positionB)}) expecting False, actual {value}")
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

  rect = Rect(32, 32)
  positionA = Vector(0, 0)
  positionB = Vector(0, 0)
  positionC = Vector(0, 64)
  positionD = Vector(0, 256)
  bodyA = Body(0, positionA, rect)
  bodyB = Body(1, positionB, rect)
  bodyC = Body(2, positionC, rect)
  bodyD = Body(3, positionD, rect)


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

  value = space.get(positionA, rect)
  print(f"Space test: get(positionA, rect) expecting [{repr(bodyA)}, {repr(bodyB)}], actual {value}")
  for v in value:
    if v.id == bodyA.id or v.id == bodyB.id:
      pass
    else:
      print(f"Fail {v.id}")
      passing = False

  value = space.get(positionC, rect)
  print(f"Space test: get(positionC, rect) expecting [{repr(bodyC)}], actual {value}")
  for v in value:
    if v.id != bodyC.id:
      print("Fail")
      passing = False

  value = space.get_body(bodyA)
  print(f"Space test: get_body(bodyA) expecting [{repr(bodyB)}], actual {value}")
  for v in value:
    if v.id != bodyB.id:
      print("Fail")
      passing = False

  value = space.get_body(bodyD)
  print(f"Space test: get_body(bodyD) expecting [], actual {value}")
  if value != []:
    print("Fail")
    passing = False

  value = space.check_two(bodyA, bodyB)
  print(f"Space test: check_two(bodyA, bodyB) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  value = space.check_two(bodyC, bodyD)
  print(f"Space test: check_two(bodyC, bodyD) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  value = space.check(bodyA)
  print(f"Space test: check(bodyA) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  value = space.check(bodyC)
  print(f"Space test: check(bodyC) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  bodyD.place(0, 0)
  space.place(bodyD, (0, 0))
  print("Space test: place(bodyD, (0, 0))")

  value = space.get_body(bodyA)
  print(f"Space test: get_body(bodyA) expecting [{repr(bodyB)}, {repr(bodyD)}], actual {value}")
  for v in value:
    if v.id == bodyB.id or v.id == bodyD.id:
      pass
    else:
      print("Fail")
      passing = False

  space.delete(bodyA)
  print("Space test: delete(bodyA)")

  value = space.get_body(bodyB)
  print(f"Space test: get_body(bodyB) expecting [{repr(bodyD)}], actual {value}")
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

  class Entity(Body):
    def __init__(self, id, position):
      shape = Rect(32, 32)
      super().__init__(id, position, shape)

  class Objects(Controller):
    def __init__(self, size):
      super().__init__(size)
      self.factory[0] = Entity

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
      print(f"body {body.id} at {str(body.position)}")

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

  objects = Objects(64)

  bodyA = objects.make(Entity, 0, 0)
  print(f"Controller test: make(Entity, 0, 0) expecting id 0, actual {bodyA.id}")
  if bodyA.id != 0:
    print("Fail")
    passing = False

  bodyB = objects.make(Entity, 0, 0, dx=1)
  print(f"Controller test: make(Entity, 0, 0, dx=1) expecting id 1, actual {bodyB.id}")
  if bodyB.id != 1:
    print("Fail")
    passing = False

  bodyC = objects.make_key(0, 0, 0, dy=1)
  print(f"Controller test: make_key(0, 0, 0, dy=1) expecting id 2, actual {bodyC.id}")
  if bodyC.id != 2:
    print("Fail")
    passing = False

  bodyD = objects.make_key(0, 0, 0)
  print(f"Controller test: make_key(Entity, 0, 0) expecting id 3, actual {bodyD.id}")
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
    print("pysics test: Complete, all tests passed")
  else:
    print("pysics test: Incomplete, some tests failed")

test()

clock = Clock(100) 
sync_clock = SyncClock()