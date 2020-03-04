

class Shape:
   """
   Abstract Base Shape that other shapes extend from. 
   Shapes are simple data structures that describe the physical properties of an body to a Collider.
   Note that shapes do not have a position, thus all bodies with the same shape can use the same Shape instance
   """
   pass


class Rect(Shape):
   """
   :param w: Width
   :param h: Height
   :type w: int
   :type h: int

   A Rectangle
   Treated as Axis-Aligned Bounding Boxes by the Collider.
   """
   def __init__(self, w, h):      
      self.w = w #: int, Width, extending up
      self.h = h #: int, Height, extending to the right


class Circle(Shape):
   """
   :param r: Radius
   :type r: int

   A Circle
   """
   def __init__(self, r):
      self.r = r #: int, Radius, extending from the center.


