

class Index:
   """
   Indexing system for assigning unique IDs to bodies.

   Index keeps track what number to assign to new entities.

   TODO move object list keeping and retrival here? Probably
   """

   def __init__(self):
      self.count = -1 #: The ID to be used for the next new body
      self.free = [] #: A list of free IDs for reuse
      
   def get(self):
      """
      :return: A unique id
      :rtype: int

      Gets a unique identifer for this index. Freed ids are assigned first, in first-in-last-out order.
      """
      if len(self.free) == 0:
         self.count += 1
         return self.count
      else:
         value = self.free[-1]
         self.free.pop()
         return value
         
   def delete(self, id):
      """
      :param id: Previously assigned id to be returned to the system
      :type id: int

      Frees an identifer to be reused.
      """
      if id <= self.count:
         self.free.append(id)
      
