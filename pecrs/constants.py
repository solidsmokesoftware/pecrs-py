from client.source.pysics.vector import Vector

"""
These are some common constants useful to the system
"""

"""
Simple direction constants
"""
UP = 1 #: Int, the numerical representation for the direction of up
DOWN = -1 #: Int, the numerical representation for the direction of down
RIGHT = 1 #: Int, the numerical representation for the direction of right
LEFT = -1 #: Int, the numerical representation for the direction of left


"""
Vector direction constants
"""
NONE_VEC = Vector(0, 0) #: Vector, a nuteral vector
UP_VEC = Vector(0, 1) #: Vector, A vector pointing up
DOWN_VEC = Vector(0, -1) #: Vector, A vector pointing down
RIGHT_VEC = Vector(1, 0) #: Vector, A vector pointing right
LEFT_VEC = Vector(-1, 0) #: Vector, A vector pointing left
UR_VEC = Vector(1, 1) #: Vector, A vector pointing up and right
UL_VEC = Vector(-1, 1) #: Vector, A vector pointing up and left
DR_VEC = Vector(1, -1) #: Vector, A vector pointing down and right
DL_VEC = Vector(-1, -1) #: Vector, A vector pointing down and left


"""
Degrees are the angle in degrees from RIGHT_VEC eg vec.angle(RIGHT_VEC)
"""
LEFT_DEG = 180.0 #:Float, Degrees LEFT_VEC is from RIGHT_VEC
RIGHT_DEG = 0.0 #:Float, Degrees RIGHT_VEC is from RIGHT_VEC
UP_DEG = -90.0 #:Float, Degrees UP_VEC is from RIGHT_VEC
DOWN_DEG = 90 #:Float, Degrees DOWN_VEC is from RIGHT_VEC
UR_DEG = -45.0 #:Float, Degrees UR_VEC is from RIGHT_VEC
UL_DEG = -135.0 #:Float, Degrees UL_VEC is from RIGHT_VEC
DR_DEG = 45.0 #:Float, Degrees DR_VEC is from RIGHT_VEC
DL_DEG = 135.0 #:Float, Degrees DL_VEC is from RIGHT_VEC
