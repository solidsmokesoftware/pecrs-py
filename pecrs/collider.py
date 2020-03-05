
from pecrs.shape import *


class Collider:
   """
   Collider handles collisions between two shapes at two given positions. Positions are Vectors
   Note that the collider is abstract and low-level, dealing with any set of shapes and positions rather than bodies in space.
   """

   def dist(self, shape, pos, shape_other, pos_other):
      """
      :param shape: Shape of the first body
      :param pos: Position of the first body
      :param shape_other: Shape of the second body
      :param pos_other: Position of the second body
      :type shape: Shape
      :type pos: Vector
      :type shape_other: Shape
      :type pos_other: Vector
      :return: x and y distance
      :rtype: Tuple(float, float)

      Distance between two shapes from edge to edge IIRC.

      TODO This might not be working correctly. Probably don't use it.
      """
      if type(shape) == Rect:
         w = shape.w
         h = shape.h

      elif type(shape) == Circle:
         w = shape.r
         h = shape.r

      if type(shape_other) == Rect:
         wo = shape.w
         ho = shape.h
      
      elif type(shape_other) == Circle:
         wo = shape.r
         ho = shape.r

      if pos.x > pos_other.x:
         xd = pos_other.x + wo - pos.x
      else:
         xd = pos.x + w - pos_other.x
    
      if pos.y > pos_other.y:
         yd = pos_other.y + ho - pos.y
      else:
         yd = pos.y + h - pos_other.y
    
      return xd, yd

   def check(self, shape, pos, shape_other, pos_other):
      """
      :param shape: Shape of the first body
      :param pos: Position of the first body
      :param shape_other: Shape of the second body
      :param pos_other: Position of the second body
      :type shape: Shape
      :type pos: Vector
      :type shape_other: Shape
      :type pos_other: Vector
      :return: True if there is a collision, False is not
      :rtype: bool

      Checks for a collision between any two shapes at two positions. 
      """
      if type(shape) == Rect:
         if type(shape_other) == Rect:
            return self.rect_rect(shape, pos, shape_other, pos_other)
         elif type(shape_other) == Circle:
            return self.rect_circle(shape, pos, shape_other, pos_other)
      elif type(shape) == Circle:
         if type(shape_other) == Rect:
            return self.circle_rect(shape, pos, shape_other, pos_other)
         elif type(shape_other) == Circle:
            return self.circle_circle(shape, pos, shape_other, pos_other)

   def rect_rect(self, shape, pos, shape_other, pos_other):
      """
      :param shape: Shape of the first body
      :param pos: Position of the first body
      :param shape_other: Shape of the second body
      :param pos_other: Position of the second body
      :type shape: Rect
      :type pos: Vector
      :type shape_other: Rect
      :type pos_other: Vector
      :return: True if there is a collision, False is not
      :rtype: bool

      Checks for a collision between two rects at two positions.
      """
      if pos.x < pos_other.x + shape_other.w and pos.x + shape.w > pos_other.x and pos.y < pos_other.y + shape_other.h and pos.y + shape.h > pos_other.y:
         return True
      else:
         return False

   def rect_circle(self, shape, pos, shape_other, pos_other):
      """
      :param shape: Shape of the first body
      :param pos: Position of the first body
      :param shape_other: Shape of the second body
      :param pos_other: Position of the second body
      :type shape: Rect
      :type pos: Vector
      :type shape_other: Circle
      :type pos_other: Vector
      :return: True if there is a collision, False is not
      :rtype: bool

      Checks for a collision between a rect and a circle at two positions.
      """
      if pos_other.x < pos.x:
         x = pos.x
      elif pos_other.x > pos.x + shape.w:
         x = pos.x + shape.w
      else:
         x = pos_other.x

      if pos_other.y < pos.y:
         y = pos.y
      elif pos_other.y > pos.y + shape.h:
         y = pos.y + shape.h
      else:
         y = pos_other.y

      dx = x - pos_other.x
      dy = y - pos_other.y
      if dx * dx + dy * dy < shape_other.r * shape_other.r:
         return True
      else:
         return False

   def circle_rect(self, shape, pos, shape_other, pos_other):
      """
      :param shape: Shape of the first body
      :param pos: Position of the first body
      :param shape_other: Shape of the second body
      :param pos_other: Position of the second body
      :type shape: Circle
      :type pos: Vector
      :type shape_other: Rect
      :type pos_other: Vector
      :return: True if there is a collision, False is not
      :rtype: bool

      Checks for a collision between a circle and a rect at two positions.
      """
      return self.rect_circle(shape_other, pos_other, shape, pos)

   def circle_circle(self, shape, pos, shape_other, pos_other):
      """
      :param shape: Shape of the first body
      :param pos: Position of the first body
      :param shape_other: Shape of the second body
      :param pos_other: Position of the second body
      :type shape: Circle
      :type pos: Vector
      :type shape_other: Circle
      :type pos_other: Vector
      :return: True if there is a collision, False is not
      :rtype: bool

      Checks for a collision between a two circles at two positions.
      """
      dx = pos.x - pos_other.x
      dy = pos.y - pos_other.y
      rs = shape.r + shape_other.r
      if dx * dx + dy * dy < rs * rs:
         return True
      else:
         return False

