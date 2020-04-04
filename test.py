from pecrs.index import Index
from pecrs.spatialhash import SpatialHash
from pecrs.space import Space
from pecrs.shape import Rect
from pecrs.shape import Circle
from pecrs.collider import Collider
from pecrs.clock import Clock
from pecrs.clock import SyncClock

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

  c = index.next()
  print(f"Index test: next() expecting 2, actual {c}")
  if c != 2:
    print("Fail")
    passing = False

  d = index.next()
  print(f"Index test: next() expecting 3, actual {d}")
  if d != 3:
    print("Fail")
    passing = False

  index.delete(a)
  print(f"Index test: delete({a})")

  e = index.next()
  print(f"Index test: next() expecting 0, actual {e}")
  if e != 0:
    print("Fail")
    passing = False

  index.delete(b)
  print(f"Index test: delete({b})")

  f = index.next()
  print(f"Index test: next() expecting 1, actual {f}")
  if f != 1:
    print("Fail")
    passing = False

  g = index.next()
  print(f"Index test: next() expecting 4, actual {g}")
  if g != 4:
    print("Fail")
    passing = False

  h = index.next()
  print(f"Index test: next() expecting 5, actual {h}")
  if h != 5:
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
  print(f"Space test: add(rectA) id {space.ids[rectA]}: {rectA}")
  space.add(rectB)
  print(f"Space test: add(rectB) id {space.ids[rectB]}: {rectB}")
  space.add(rectC)
  print(f"Space test: add(rectC) id {space.ids[rectC]}: {rectC}")
  space.add(rectD)
  print(f"Space test: add(rectD) id {space.ids[rectD]}: {rectD}")

  value = space.has(rectA)
  print(f"Space test: has(rectA)) expecting True, actual {value}")
  if value != True:
    print("Fail")
    passing = False

  value = space.collisions_at(0, 0, 32, 32)
  print(f"Space test: collisions_at(0, 0, 32, 32) expecting [{rectA}, {rectB}]")
  for v in value:
    if v == rectA or v == rectB:
      pass
    else:
      print(f"Fail {v}")
      passing = False

  value = space.collisions_at(0, 64)
  print(f"Space test: colliding_at(0, 64) expecting [{rectC}]")
  for v in value:
    if v != rectC:
      print(f"Fail {v}")
      passing = False

  value = space.collisions_with(rectA)
  print(f"Space test: collisions_with(rectA) expecting [{rectB}]")
  for v in value:
    if v != rectB:
      print(f"Fail {v}")
      passing = False

  value = space.collisions_with(rectD)
  print(f"Space test: collisions_with(rectD) expecting []")
  if value != []:
    print(f"Fail {value}")
    passing = False

  value = space.check_two(rectA, rectB)
  print(f"Space test: check_two(rectA, rectB) expecting True")
  if value != True:
    print("Fail")
    passing = False

  value = space.check_two(rectC, rectD)
  print(f"Space test: check_two(rectC, rectD) expecting False")
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
  print(f"Space test: collisions_with(rectA) expecting [{rectB}, {rectD}]")
  for v in value:
    if v == rectB or v == rectD:
      pass
    else:
      print(f"Fail {v}")
      passing = False
  
  area = space.areas[rectA]
  space.delete(rectA)
  print("Space test: delete(rectA)")
  value = space.grid.get(area)
  for v in value:
    if v == rectA:
      print("Fail")

  value = space.collisions_with(rectB)
  print(f"Space test: collisions_with(rectB) expecting [{rectD}]")
  for v in value:
    if v == rectD:
      pass
    else:
      print(f"Fail {v}")
      passing = False

  print("Space test group testing")
  space = Space()
  headA = Rect(0, 0, 32, 32)
  bodyA = Rect(0, 30, 32, 32)
  headB = Rect(64, 0, 32, 32)
  bodyB = Rect(64, 32, 32, 32)
  space.add(headA, group="a")
  space.add(bodyA, group="a")
  space.start_group("a")
  space.add(headB, group="b")
  space.add(bodyB, group="b")

  value = space.collisions_with_group("a")
  print(f"Space test: collisions_with_group(\"a\") expecting [], actual {value}")
  if value != []:
    print("Fail")
    passing = False
  
  space.move_group("a", 1)
  print(f"Space test: group a position {headA.position}, {bodyA.position}")
  print(f"Space test: group b position {headB.position}, {bodyB.position}")

  space.place_group("b", 1, 1)
  print(f"Space test: group a position {headA.position}, {bodyA.position}")
  print(f"Space test: group b position {headB.position}, {bodyB.position}")

  value = space.collisions_with_group("a")
  print(f"Space test: collisions_with_group(\"a\") expecting [...], actual {value}")
  for v in value:
    if v == headB or v == bodyB:
      pass
    else:
      print(f"Fail {v}")
      passing = False
  
  space.turn_group("a", (1, 0))
  space.turn(bodyB, (-1, 0))
  space.turn(headB, (-1, 0))

  space.step(1)
  print(f"Space test: group a position {headA.position}, {bodyA.position}")
  print(f"Space test: group b position {headB.position}, {bodyB.position}")

  value = space.collisions_with_group("b")
  print(f"Space test: collisions_with_group(\"b\") expecting [...], actual {value}")
  for v in value:
    if v == headA or v == bodyA:
      pass
    else:
      print(f"Fail {v}")
      passing = False

  space.step(10)
  print(f"Space test: group a position {headA.position}, {bodyA.position}")
  print(f"Space test: group b position {headB.position}, {bodyB.position}")
  
  value = space.collisions_with_group("a")
  print(f"Space test: collisions_with_group(\"a\") expecting [...], actual {value}")
  for v in value:
    if v == headB or v == bodyB:
      pass
    else:
      print(f"Fail {v}")
      passing = False

  space.delete_group("b") 

  value = space.collisions_with_group("a")
  print(f"Space test: collisions_with_group(\"a\") expecting [...], actual {value}")
  for v in value:
    print(f"Fail {v}")
    passing = False

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

  if passing:
    print("pecrs version {pecrs.version} test: Complete, all tests passed")
  else:
    print("pecrs version {pecrs.version} test: Incomplete, some tests failed")

test()

clock = Clock(100) 
sync_clock = SyncClock()