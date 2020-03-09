
from pecrs.shape import *


class Collider:
   """
   Collider handles collisions between two objects with physical dimensions.
   Note that the collider is abstract and low-level, dealing with any set of positions and dimensions.
   """

   def check(self, shape, other):
      """
      :param shape: Shape of the first object
      :param other: Shape of the second object
      :type shape: Shape
      :type other: Shape
      :return: True if there is a collision, False is not
      :rtype: bool

      Checks for a collision between any two shapes. Determines what the shapes are and sends them to the appropriate collision method.
      If you already know the shape of your objects, use a more direct method.
      """
      if type(shape) == Rect:
         if type(other) == Rect:
            return self.rect_rect(shape.width, shape.height, shape.position[0], shape.position[1], other.width, other.height, other.position[0], other.position[1])
         elif type(other) == Circle:
            return self.rect_circle(shape.width, shape.height, shape.position[0], shape.position[1], other.radius, other.position[0], other.position[1])
      elif type(shape) == Circle:
         if type(other) == Rect:
            return self.circle_rect(shape.radius, shape.position[0], shape.position[1], other.width, other.height, other.position[0], other.position[1])
         elif type(other) == Circle:
            return self.circle_circle(shape.radius, shape.position[0], shape.position[1], other.radius, other.position[0], other.position[1])

   def check_rects(self, shape, other):
      """
      :param shape: Shape of the first Rect
      :param other: Shape of the second Rect
      :type shape: Rect
      :type other: Rect
      :return: True if there is a collision, False is not
      :rtype: bool

      Checks for a collision between any two Rects. This is a higher level interface for Collider.rect_rect().
      Note that Pyglet sprites are effectively Rects and can be used interchangably here.
      """
      return self.rect_rect(shape.width, shape.height, shape.position[0], shape.position[1], other.width, other.height, other.position[0], other.position[1])

   def check_circles(self, shape, other):
      """
      :param shape: Shape of the first Circle
      :param other: Shape of the second Circle
      :type shape: Circle
      :type other: Circle
      :return: True if there is a collision, False is not
      :rtype: bool

      Checks for a collision between any two Circles. This is a higher level interface for Collider.circle_circle().
      """
      return self.circle_circle(shape.radius, shape.position[0], shape.position[1], other.radius, other.position[0], other.position[1])

   def rect_rect(self, w, h, x, y, wo, ho, xo, yo):
      """
      :param w: Width of the first Rect
      :param h: Height of the first Rect
      :param x: x position of the first Rect
      :param y: y position of the first Rect
      :param wo: Width of the second Rect
      :param ho: Height of the second Rect
      :param xo: x position of the second Rect
      :param yo: y position of the second Rect
      :type w: Int
      :type h: Int
      :type x: Int
      :type y: Int
      :type wo: Int
      :type ho: Int
      :type xo: Int
      :type yo: Int

      Checks for a collision between two Rects in abstract.
      """
      if x < xo + wo and x + w > xo and y < yo + ho and y + h > yo:
         return True
      else:
         return False

   def rect_circle(self, w, h, x, y, ro, xo, yo):
      """
      :param w: Width of the first Rect
      :param h: Height of the first Rect
      :param x: x position of the first Rect
      :param y: y position of the first Rect
      :param ro: Radius of the second Circle
      :param xo: x position of the second Circle
      :param yo: y position of the second Circle
      :type w: Int
      :type h: Int
      :type x: Int
      :type y: Int
      :type ro: Int
      :type xo: Int
      :type yo: Int

      Checks for a collision between a Rect and a Circle in abstract.
      """
      if xo < x:
         x = x
      elif xo > x + w:
         x = x + w
      else:
         x = xo

      if yo < y:
         y = y
      elif yo > y + h:
         y = y + h
      else:
         y = yo

      dx = x - xo
      dy = y - yo
      if dx * dx + dy * dy < ro * ro:
         return True
      else:
         return False

   def circle_rect(self, r, x, y, wo, ho, xo, yo):
      """
      :param r: Radius of the first Circle
      :param x: x position of the first Circle
      :param y: y position of the first Circle
      :param wo: Width of the second Rect
      :param ho: Height of the second Rect
      :param xo: x position of the second Rect
      :param yo: y position of the second Rect
      :type r: Int
      :type x: Int
      :type y: Int
      :type wo: Int
      :type ho: Int
      :type xo: Int
      :type yo: Int

      Checks for a collision between a Circle and a Rect in abstract. Interface for Collider.rect_circle
      """
      return self.rect_circle(wo, ho, xo, yo, r, x, y)

   def circle_circle(self, r, x, y, ro, xo, yo):
      """
      :param r: Radius of the first Circle
      :param x: x position of the first Circle
      :param y: y position of the first Circle
      :param ro: Radius of the second Circle
      :param xo: x position of the second Circle
      :param yo: y position of the second Circle
      :type r: Int
      :type x: Int
      :type y: Int
      :type wo: Int
      :type ho: Int
      :type xo: Int
      :type yo: Int

      Checks for a collision between any two Circles abstract.
      """
      dx = x - xo
      dy = y - yo
      rs = r + ro
      if dx * dx + dy * dy < rs * rs:
         return True
      else:
         return False

