
import ctypes
import time


class Clock:
   """
   :param rate: Minimum amount of time before the next tick can occur
   :type rate: float

   Keeps track of time through polling tick
   """

   def __init__(self, rate):
      self.rate = rate #: float, Minimum amount of time before the next tick can occur
      self.time = ctypes.c_ulong(0) #: ctypes.c_ulong, Number of ticks. Using ctypes for free rollover 
      self.last = time.time() #: time.time, Time of the last tick

   def get_time(self):
      """
      Get the number of ticks that have elapsed
      :return: Number of ticks that have elapsed
      :rtype: int
      """
      return self.time.value

   def tick(self):
      """
      :return: delta or None
      :rtype: float or None
   
      Attemps to advance the system clock. 
      Delta is the ratio of time that has passed since the tick. 
      For example if your tick rate is 100ms, and your tick happens 150ms after your last tick, your delta will be 1.5
      You probably are going to want to use this one for timing in games
      """

      now = time.time()
      value = now - self.last
      if value > self.rate:
         delta = value / self.rate
         self.time.value += 1
         self.last = now
         return delta
      else:
         return None

   def tick_time(self):
      """
      :return: Current time
      :rtype: int

      Attemps to advance the system clock.
      Always returns the time.
      """
      now = time.time()
      value = now - self.last
      if value > self.rate:
         self.last = now
         self.time.value += 1
      return value

   def tick_check(self):
      """
      :return: True if rate time has elapsed since the last tick, False if not
      :rtype: bool

      Attemps to advance the system clock. 
      """
      now = time.time()
      if now - self.last > self.rate:
         self.last = now
         self.time.value += 1
         return True
      else:
         return False


class SyncClock:
   """
   A Clock for syncing values from a master Clock.
   """

   def __init__(self):
      self.time = 0

   def get_time(self):
      """
      :return: The current time
      :rtype: int

      Gets the current time
      """
      return self.time