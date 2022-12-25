# Reference: https://github.com/pagekeytech/education/blob/master/HashTable/hashtable.py

import time
import random

# Create a list of the next prime numbers from 2^10 to 2^30
primes = [1031, 2053, 4099, 8209, 16411, 32771, 65537, 131101, 262147, 524309, 1048583, 2097169, 4194319, 8388617, 16777259, 33554467, 67108879, 134217757, 268435459, 536870923, 1073741827]

class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
class HashTable:
	def __init__(self, j):
		self.j = j
		# Set capacity as the next prime number larger than 2^j
		self.capacity = primes[j-10]
		self.size = 0
		self.buckets = [None]*self.capacity

	def hash(self, key): # h(x) = (x1 * r1 + x2 * r2) % M 
		hashsum = 0
		for idx, c in enumerate(key): # For each character (bit) in the key
			# hashsum: (x1 * r1 + x2 * r2); M: self.capacity
			hashsum += random.randint(0,self.capacity) * ord(c)
		hashout = hashsum % self.capacity
		return hashout

	def insert(self, key, value):
		# 1. Increase size
		self.size += 1
		# 2. Compute index of key and visit the index
		index = self.hash(key)
		node = self.buckets[index]
		# 3. Create a node and add the key-value pair
		if node is None:
			self.buckets[index] = Node(key, value)
			return
		prev = node
		while node is not None:
			prev = node
			node = node.next
		prev.next = Node(key, value)

	def find(self, key):
		index = self.hash(key)
		node = self.buckets[index]
		while node is not None and node.key != key:
			node = node.next
		if node is None:
			return None
		else:
			return node.value

if __name__ == '__main__':
  insert_times = []
  search_times = []
  for j in range(10, 31):
    print("{2^"+str(j)+" data}")
    HT = HashTable(j)
    start = time.process_time()
    for i in range(2**j):
      key = random.randint(1, 2**30)
      HT.insert(str(key), key)
    end = time.process_time()
    insert_time = round(end - start, 2)
    insert_times.append(insert_time)
    # print("Insert = {:.2f} seconds".format(insert_time))
    print(insert_times)

    open = time.process_time()
    for i in range(10**5):
      key = str(random.randint(1, 2**30))
      HT.find(key)
    close = time.process_time()
    search_time = round(close - open, 2)
    search_times.append(search_time)
    # print("Search = {:.2f} seconds".format(search_time))
    print(search_times)
    # print("----------------------------------------")