
import math

###### DEPRECIATION ########
# Vector is being depreciated in favor of using a tuple(int, int) like Pyglet's sprites.
# Stop using Vector immediately and remove references to Vector as soon as possible
#TODO remove Vector
# WARNING

class Vector:
   """
   :param x: A position in space on the horizontal plane
   :param y: A position in space on the vertical plane
   :type x: int
   :type y: int

   A typical Vector datatype
   """
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def __add__(self, other):
      """
      :param other: A second vector
      :param type: Vector()

      Add two vectors together. Changes the first vector
      """
      self.x += other.x
      self.y += other.y

   def __sub__(self, other):
      """
      :param other: A second vector
      :param type: Vector()

      Substract two vectors from each other. Changes the first vector
      """
      self.x -= other.x
      self.y -= other.y

   def __mul__(self, other):
      """
      
      Multiples a vector by a scalar value
      other is a number
      """
      self.x *= other
      self.y *= other

   def __truediv__(self, other):
      """
      Divides a vector by a scalar value
      other is a number
      """
      self.x /= other
      self.y /= other

   def __floordiv__(self, other): #Scalar
      """
      Floor division by a scalar value
      other is a number
      """
      self.x = self.x // other
      self.y = self.y // other

   def __mod__(self, other): #Scalar
      """
      Modulus by a scalar value
      other is a number
      """
      self.x = self.x % other
      self.y = self.y % other

   def __pow__(self, other): #Scalar
      """
      Exponent by a scalar value
      other is a number
      """
      self.x = self.x ** other
      self.y = self.y ** other

   def __eq__(self, other):
      """
      :param other: A second vector
      :param type: Vector()
      :return: True if x and y are the same for both vectors, False if not
      :rtype: bool

      Equality between two vectors
      """
      if self.x == other.x and self.y == other.y:
         return True
      else:
         return False

   def __ne__(self, other):
      if self.x != other.x and self.y != other.y:
         return True
      else:
         return False

   def __lt__(self, other):
      if self.x < other.x and self.y < other.y:
         return True
      else:
         return False

   def __gt__(self, other):
      if self.x > other.x and self.y > other.y:
         return True
      else:
         return False

   def __le__(self, other):
      if self.x <= other.x and self.y <= other.y:
         return True
      else:
         return False

   def __ge__(self, other):
      if self.x >= other.x and self.y >= other.y:
         return True
      else:
         return False

   def dot(self, other):
      """
      :param other: A second vector
      :param type: Vector()
      :return: Dot product of two vectors
      :rtype: float

      Dot product of two vectors.
      """
      return self.x * other.x + self.y * other.y

   def cross(self, other):
      """
      :param other: A second vector
      :param type: Vector()
      :return: Cross product of two vectors
      :rtype: float

      Cross product of two vectors.
      """
      return self.x * other.y - self.y * other.x

   def mag_square(self):
      """
      :return: Square magnitude of the vector.
      :rtype: float

      Square magnitude of the vector.
      """
      return self.x * self.x + self.y * self.y

   def mag(self):
      """
      :return: Magnitude of the vector.
      :rtype: float
      
      Magnitude of the vector.
      """
      return math.sqrt(self.mag_square())

   def angle_self(self):
      """
      :return: Angle of the vector.
      :rtype: float

      Angle of the vector.
      returns a number.
      """
      return math.atan2(self.x, self.y)

   def normal(self):
      """
      :return: Normal of the vector.
      :rtype: float
      
      Normal of the vector.
      """
      len = self.mag_square()
      if len != 0:
         len = math.sqrt(len)
         self.x = self.x // len
         self.y = self.y // len
      else:
         self.x = 0
         self.y = 0

   def dist_square(self, x, y):
      """
      :param x: A position in space
      :param y: A position in space
      :type x: int
      :type y: int
      :return: Distance squared from x, y.
      :rtype: float
      
      Distance squared from x, y. Faster than dist() for relative distance comparisons
      """
      xd = self.x - x
      yd = self.y - y
      return xd * xd + yd * yd

   def dist(self, x, y):
      """
      :param x: A position in space
      :param y: A position in space
      :type x: int
      :type y: int
      :return: Distance squared from x, y.
      :rtype: float
      
      Distance from x, y
      """
      return math.sqrt(self.dist_square(x, y))

   def angle_rads(self, other):
      """
      :param other: Second vector to find the angle to
      :type other: Vector()
      :return: Angle to the second vector in radians
      :rtype: float

      Angle to a vector in radians
      """
      return math.atan2(self.cross(other), self.dot(other))

   def angle(self, other):
      """
      :param other: Second vector to find the angle to
      :type other: Vector()
      :return: Angle to the second vector in degrees
      :rtype: float

      Angle to a vector in degrees
      """
      return math.degrees(math.atan2(self.cross(other), self.dot(other)))

   def angle_point(self, other):
      """
      :param other: Second vector to find the angle to
      :type other: Vector()
      :return: Angle point to the second vector
      :rtype: float

      Angle point to a vector
      """
      return math.atan2(self.x - other.y, self.x - other.x)

   def abs(self):
      """
      Absolute value.
      Sets x and y to positive values.
      """
      self.x = abs(self.x)
      self.y = abs(self.y)

   def project(self, other):
      """
      :param other: Second vector to project from
      :type other: Vector()
      :return: Value of the projection
      :rtype: float

      Projection from another vector
      """
      return other * (self.dot(other) / other.mag_square())

   def clamp(self, min, max):
      """
      :param min: Minimum value of x and y
      :param max: Maximum values of x and y
      :type min: int
      :type max: int

      Sets the vector to a minimum and maximum value
      """
      if self.x < min:
         self.x = min
      elif self. x > max:
         self.x = max

      if self.y < min:
         self.y = min
      elif self.y > max:
         self.y = max

   def move(other, delta):
      """
      :param other: Direction to move in
      :param delta: Units of time to move in
      :type other: Vector()
      :type delta: float

      Move in the direction of other by delta units
      """
      self.x += other.x * delta
      self.y += other.y * delta 

   def __str__(self):
      """
      :return: String representation of the vector
      :rtype: string
      
      String representation of a vector
      """
      return "{int(self.x)}:{int(self.y)}"

