"""
Array of sorted Arrays
References: 
(1) BinarySearch: https://www.programiz.com/dsa/binary-search
(2) Merge: https://levelup.gitconnected.com/merge-two-sorted-ASAays-in-python-a6851f8ff2e2
"""

import time
import random

def BinarySearch(Array, x):
    low = 0
    high = len(Array)-1

    while low <= high:
      mid = low + (high - low)//2
      if Array[mid] == x:
          return mid
      elif Array[mid] < x:
          low = mid + 1
      else:
          high = mid - 1
    return -1

    if (Array[low] == x): # Check when low == high
      return low

def Merge(V1, V2):
  return sorted(V1 + V2)

class ASA(list):
  def __init__(self):
    self._D = [] # Initialize _D as a temporary array used for merging
    self.max_size = 0 

  def insert(self, x):
    if self.max_size == 0: # If ASA is empty, append [x] to ASA
      self.append([x]) 
      self.max_size += 1 # increase max_size 
    else:
      if len(self[0]) == 0: # If ASA[0] is an empty array, append x to ASA[0]
        self[0].append(x)
      else:
        self._D.append(x) # If ASA[0] is NOT empty, append x to _D for merging
        for i in range(0,self.max_size): 
          if len(self[i])!= 0: # If ASA[i] isn't empty, merge ASA[i] and _D into _D
            self._D = Merge(self[i],self._D)
            self[i].clear() # Clear ASA[i] after merging
          else:
            self[i] = self._D # If ASA[0] is empty, ASA[i] = _D
            self._D.clear() # Clear _D for another round
            break
        if len(self._D)!= 0: # If _D is NOT empty, append _D to ASA
          self.append(self._D) 
          self.max_size += 1

  def search(self, x):
    for i in range(0,self.max_size):
      if len(self[i])!=0 and BinarySearch(self[i], x)!=-1:
        return True
    return False

  def print(self):
    for i in range(0,self.max_size):
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
    for i in range(10**5):
        ASA.search(random.randint(1, 2**30))
    close = time.time()
    search_time = round(close - open, 2)
    search_times.append(search_time)
    # print("Search = {:.2f} seconds".format(search_time))
    print(search_times)
    # print("----------------------------------------")