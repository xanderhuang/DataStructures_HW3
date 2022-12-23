"""
Array of sorted arrays
References: 
(1) BinarySearch: https://www.programiz.com/dsa/binary-search
(2) Merge: https://levelup.gitconnected.com/merge-two-sorted-arrays-in-python-a6851f8ff2e2
"""

import time
import random

def BinarySearch(array, x):
    low = 0
    high = len(array)-1

    while low <= high:
      mid = low + (high - low)//2
      if array[mid] == x:
          return mid
      elif array[mid] < x:
          low = mid + 1
      else:
          high = mid - 1
    return -1

    if (array[low] == x): # Check when low == high
      return low

def Merge(V1, V2):
  return sorted(V1 + V2)

class ASA(list):
  def __init__(self):
    self._D = [] # temp array
    self.maxsize = 0

  def insert(self, x):
    if self.maxsize == 0:
      self.append([x])
      self.maxsize += 1
    else:
      if len(self[0]) == 0:
        self[0].append(x)
      else:
        self._D.append(x)
        for i in range(0,self.maxsize):
          if len(self[i])!= 0:
            self._D = Merge(self[i],self._D)
            self[i].clear()
          else:
            self[i] = self._D 
            self._D.clear()
            break
        if len(self._D)!= 0:
          self.append(self._D)
          self.maxsize += 1

  def search(self, x):
    for i in range(0,self.maxsize):
      if len(self[i])!=0 and BinarySearch(self[i], x)!=-1:
        return True
    return False

  def print(self):
    for i in range(0,self.maxsize):
      for j in range(0,len(self[i])):
        print('{:2}'.format(str(self[i][j])), end = '')
      print()

if __name__ == '__main__':
  insert_times = []
  search_times = []
  ASA = ASA()
  for j in range(10, 31):
    print("{2^"+str(j)+" data}")
    start = time.time()
    for i in range(2**j):
        ASA.insert(random.randint(1, 2**30))
    end = time.time()
    insert_time = round(end - start, 2)
    insert_times.append(insert_time)
    # print("Insert = {:.2f} seconds".format(insert_time))
    print(insert_times)

    open = time.time()
    for i in range(2**j):
        ASA.search(random.randint(1, 2**30))
    close = time.time()
    search_time = round(close - open, 2)
    search_times.append(search_time)
    # print("Search = {:.2f} seconds".format(search_time))
    print(search_times)
    # print("----------------------------------------")