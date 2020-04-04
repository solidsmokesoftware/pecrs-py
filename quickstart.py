from pecrs import *

space = Space()
rectA = Rect(0, 0, 32, 32)
rectB = Rect(10, 0, 32, 32)

space.add(rectA)
space.add(rectB)

collision = space.check(rectA)
print(f"Is something colliding with rectA? {collision}")

collisions = space.collisions_with(rectB)
print(f"Who is colliding with rectB? {collisions}")

space.place(rectB, 100, 0)

collision = space.check_two(rectA, rectB)
print(f"Are rectA and rectB still colliding? {collision}")