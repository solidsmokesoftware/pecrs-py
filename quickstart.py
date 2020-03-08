from pecrs import *

controller = Controller()
shape = Rect(32, 32)
bodyA = controller.make(Body, 0, 0, shape)
bodyB = controller.make(Body, 10, 0, shape)

collision = controller.space.check(bodyA)
#print(f"Is something colliding with bodyA? {collision}")

collisions = controller.space.colliding_with(bodyB)
#print(f"Who is colliding with bodyB? {collisions}")

controller.place(bodyB, 100, 0)

collision = controller.space.check_two(bodyA, bodyB)
#print(f"Are bodyA and bodyB colliding? {collision}")
print(1)