

class Shape:
   """
   :param x: Position of the shape in the x-axis
   :param y: Position of the shape in the y-axis
   :type x: Int
   :type y: Int

   Abstract Base Shape that other shapes extend from. 
   Shapes are simple data structures that describe the physical properties of an body to a Collider.
   """
   def __init__(self, x, y):
      self.position = (x, y) #: Tuple(Int, Int), position of the shape


class Rect(Shape):
   """
   :param x: Position of the shape in the x-axis
   :param y: Position of the shape in the y-axis
   :param width: Width of the Rect
   :param height: Height of the Rect
   :type x: Int
   :type y: Int
   :type width: int
   :type height: int

   A Rectangle
   Treated as Axis-Aligned Bounding Boxes by the Collider.
   """
   def __init__(self, x, y, width, height):
      self.position = (x, y) #: Tuple(Int, Int), position of the shape
      self.width = width #: Int, Width, extending up
      self.height = height #: Int, Height, extending to the right


class Circle(Shape):
   """
   :param x: Position of the shape in the x-axis
   :param y: Position of the shape in the y-axis
   :param radius: Width of the Rect
   :type x: Int
   :type y: Int
   :type radius: int

   A Circle
   """
   def __init__(self, x, y, radius):
      self.position = (x, y) #: Tuple(Int, Int), position of the shape
      self.radius = radius #: Int, Radius, extending from the center.


