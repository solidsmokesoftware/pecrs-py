from pecrs import *

id = 0
position = Vector(100, 500)
shape = Rect(10, 10)
body = Body(id, position, shape)

id = 1
position_other = Vector(100, 495)
other = Body(id, position_other, shape)

spatial_hash_size = 128
space = Space(spatial_hash_size)

space.add(body)
space.add(other)

collision = space.check(body)
print(f"Are 0 and 1 colliding? {collision}")