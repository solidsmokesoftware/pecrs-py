

class Index:
   """
   Indexing system for assigning unique IDs to bodies.

   Index keeps track what number to assign to new entities.

   TODO move object list keeping and retrival; update docs
   """

   def __init__(self):
      self.count = -1 #: The ID to be used for the next new body
      self.free = [] #: A list of free IDs for reuse
      self.list = {} #: List of objects by thier id
      
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

   def add(self, item, id=None):
      if id == None:
         id = self.next()
      item.id = id
      self.list[id] = item

   def get(self, id):
      return self.list[id]

   def has(self, id):
      return id in self.list

   def delete(self, id):
      """
      :param id: Previously assigned id to be returned to the system
      :type id: int

      Frees an identifer to be reused.
      """
      if id in self.list:
         del self.list[id]
         self.free.append(id)
      
