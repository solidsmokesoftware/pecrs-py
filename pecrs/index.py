

class Index:
   """
   Indexing system for assigning unique IDs to bodies.

   Index keeps track what number to assign to new entities.

   TODO move object list keeping and retrival; update docs
   """

   def __init__(self):
      self.count = -1 #: The ID to be used for the next new body
      self.free = [] #: A list of free IDs for reuse
      
   def next(self):
      """
      :return: A unique id
      :rtype: int

      Gets a unique identifer for this index. Freed ids are assigned first, in first-in-last-out order.
      """
      if not self.free:
         self.count += 1
         return self.count
      else:
         return self.free.pop()

   def delete(self, id):
      """
      :param id: Previously assigned id to be returned to the system
      :type id: int

      Frees an identifer to be reused.
      """
      if id <= self.count:         
         self.free.append(id)
      
