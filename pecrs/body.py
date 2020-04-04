## Depreciated being removed


from pecrs.shape import Rect


class Body:
   """
   :param id: Identifer of the body, should be unique to an Index
   :param shapes: List of Shapes that make up the body
   :type id: Int
   :type shapes: List(Shape)
   
   The abstract base class for all bodies. Bodies are physical entities that can interact with other bodies in space.
   """
   def __init__(self, id, shapes):
      self.id = id #: Identifer of the body, should be unique
      self.shapes = shapes #: List of shapes that make up the body
      self.name = "absbody" #: string, used to communicate body type in a reader friendly way