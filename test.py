import pecrs
from pecrs import *


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

  print(f"Index test: add(Rect(), {a})")
  index.add(Rect(0, 0, 32, 32), a)

  print(f"Index test: add(Rect(), {b})")
  index.add(Rect(0, 0, 32, 32), b)

  print(f"Index test: add(Rect())")
  index.add(Rect(0, 0, 32, 32))

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

  collider.check(rectA, rectB)
  print(f"Collider test: check(rectA, rectB)")

  collider.check(rectA, circleA)
  print(f"Collider test: check(rectA, circleA)")

  collider.check(circleB, rectB)
  print(f"Collider test: check(circleB, rectB)")

  collider.check(circleA, circleB)
  print(f"Collider test: check(circleA, circleA)")

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


  value = space.has(rectA)
  print(f"Space test: has(rectA)) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  space.add(rectA)
  print("Space test: add(rectA)")
  rectB.area = (0, 0)
  space.add(rectB, False)
  print("Space test: add(rectB, False)")
  space.add(rectC)
  print("Space test: add(rectC)")
  space.add(rectD)
  print("Space test: add(rectD)")

  value = space.has(rectA)
  print(f"Space test: has(rectA)) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  value = space.has(rectA)
  print(f"Space test: has(rectB)) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  value = space.collisions_at(0, 0, 32, 32)
  print(f"Space test: collisions_at(0, 0, 32, 32) expecting [...], actual [...]")
  for v in value:
    if v == rectA or v == rectB:
      pass
    else:
      print(f"Fail {v}")
      passing = False

  value = space.collisions_at(0, 64)
  print(f"Space test: colliding_at(0, 64) expecting [...], actual [...]")
  for v in value:
    if v != rectC:
      print("Fail")
      passing = False

  value = space.collisions_with(rectA)
  print(f"Space test: collisions_with(rectA) expecting [...], actual [...]")
  for v in value:
    if v != rectB:
      print("Fail")
      passing = False

  value = space.collisions_with(rectD)
  print(f"Space test: collisions_with(rectD) expecting [...], actual [...]")
  if value != []:
    print("Fail")
    passing = False

  value = space.check_two(rectA, rectB)
  print(f"Space test: check_two(rectA, rectB) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  value = space.check_two(rectC, rectD)
  print(f"Space test: check_bodies(rectC, rectD) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  value = space.check(rectA)
  print(f"Space test: check(rectA) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  value = space.check(rectC)
  print(f"Space test: check(rectC) expecting False, actual {value}")
  if value != False:
    print("Fail")
    passing = False

  space.place(rectD, 0, 0)
  print("Space test: place(rectD, 0, 0)")

  value = space.collisions_with(rectA)
  print(f"Space test: collisions_with(rectA) expecting [...], actual [...]")
  for v in value:
    if v == rectB or v == rectD:
      pass
    else:
      print("Fail")
      passing = False

  space.delete(rectA)
  print("Space test: delete(rectA)")

  value = space.collisions_with(rectB)
  print(f"Space test: collisions_with(rectB) expecting [...], actual [...]")
  for v in value:
    if v != rectD:
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