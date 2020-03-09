from pecrs import *

controller = Controller()
bodyA = controller.make(Body, 0, 0, 32, 32)
bodyB = controller.make(Body, 10, 0, 32, 32)

collision = controller.check(bodyA)
print(f"Is something colliding with bodyA? {collision}")

collisions = controller.collisions_with(bodyB)
print(f"Who is colliding with bodyB? {collisions}")

controller.place(bodyB, 100, 0)

collision = controller.check_two(bodyA, bodyB)
print(f"Are bodyA and bodyB colliding? {collision}")