from pecrs import *

controller = Controller()
bodyA = controller.make(Body, 0, 0, 32, 32)
bodyB = controller.make(Body, 10, 0, 32, 32)

collision = controller.space.check_body(bodyA)
print(f"Is something colliding with bodyA? {collision}")

collisions = controller.space.collisions_with(bodyB)
print(f"Who is colliding with bodyB? {collisions}")

controller.place(bodyB, 100, 0)

collision = controller.space.check_bodies(bodyA, bodyB)
print(f"Are bodyA and bodyB colliding? {collision}")