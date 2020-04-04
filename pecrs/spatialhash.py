

class SpatialHash:
  """
  :param size: Size of each grid cell
  :type size: int

  A generic spatialhash
  Keeps a bucket of objects at a given scaled position
  """
  def __init__(self, size):
    self.grid = {} #: dict, Grid of buckets
    self.size = size #: int, Size of each grid cell
  
  def scale(self, x, y):
    """
    :param x: A position in to be scaled on the horizontal plane
    :param y: A position in to be scaled on the horizontal plane
    :type x: int
    :type y: int
    :return: Grid cell key for the position at x, y
    :rtype: tuple(int, int)

    Scales an x, y value to a grid cell position
    """
    return (x // self.size, y // self.size)

  def add(self, item, area):
    """
    :param item: Item to be added to the grid
    :param area: Area to add the item to
    :type item: Object
    :type area: tuple(int, int)

    Add an item to the grid at an area
    """

    if area not in self.grid:
      self.grid[area] = []
    self.grid[area].append(item)

  def add_pos(self, item, x, y):
    """
    :param item: Item to be added to the grid
    :param x: Area position
    :param y: Area position
    :type item: Object
    :type x: int
    :type y: int

    Add an item to the grid at x, y
    """
    return self.add(item, self.scale(x, y))

  def has(self, item, area=None):
    """
    :param item: Item to be added to the grid
    :param area: Area to check, checks all if None
    :type item: Object
    :type area: tuple(int, int) or None

    Checks to see if an item is in the grid
    """
    if area:
      if area in self.grid:
        if item in self.grid[area]:
          return True

    else:
      for area in self.grid:
        if item in self.grid[area]:
          return True

    return False

  def get(self, area):
    """
    :param area: Grid area
    :type area: tuple(int, int)
    :return: List of objects at position at x, y
    :rtype: list(Object)

    Get a bucket at area from the grid
    """
    if area not in self.grid:
      self.grid[area] = []
    return self.grid[area]

  def get_pos(self, x, y):
    """
    :param x: Area position
    :param y: Area position
    :type x: int
    :type y: int
    :return: List of objects at position at x, y
    :rtype: list(Object)

    Get a bucket at x, y from the grid
    """
    return self.get(self.scale(x, y))
  
  def delete(self, item, area):
    """
    :param item: Item to be removed to the grid
    :param area: Area to remove the item from
    :type item: Object
    :type area: tuple(int, int)

    Remove an item from the grid at an area
    """
    if area in self.grid:
      if item in self.grid[area]:
        self.grid[area].remove(item)
        if len(self.grid[area]) == 0:
          del self.grid[area]

  def delete_pos(self, item, x, y):
    """
    :param item: Item to be removed to the grid
    :param x: Area position
    :param y: Area position
    :type item: Object
    :type x: int
    :type y: int

    Remove an item to the grid at x, y
    """
    return self.delete(item, self.scale(x, y))

      