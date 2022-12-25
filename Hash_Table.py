# Reference: https://github.com/pagekeytech/education/blob/master/HashTable/hashtable.py

import time
import random

# a list of the next prime numbers from 2^10 to 2^30
primes = [1031, 2053, 4099, 8209, 16411, 32771, 65537, 131101, 262147, 524309, 1048583, 2097169, 4194319, 8388617, 16777259, 33554467, 67108879, 134217757, 268435459, 536870923, 1073741827]
class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
class HashTable:
	# Initialize hash table
	def __init__(self, j):
		self.j = j
		# Set capacity as the next prime number larger than 2^j
		self.capacity = primes[j-10]
		self.size = 0
		self.buckets = [None]*self.capacity
	# Generate a hash for a given key
	# Input:  key - string
	# Output: Index from 0 to self.capacity
	def hash(self, key):
		hashsum = 0
		# For each character in the key
		for idx, c in enumerate(key):
			# Add (index + length of key) ^ (current char code)
			hashsum += (idx + len(key)) ** ord(c)
			# Perform modulus to keep hashsum in range [0, self.capacity - 1]
			hashsum = hashsum % self.capacity
		return hashsum

	# Insert a key,value pair to the hashtable
	# Input:  key - string
	# 		  value - anything
	# Output: void
	def insert(self, key, value):
		# 1. Increment size
		self.size += 1
		# 2. Compute index of key
		index = self.hash(key)
		# Go to the node corresponding to the hash
		node = self.buckets[index]
		# 3. If bucket is empty:
		if node is None:
			# Create node, add it, return
			self.buckets[index] = Node(key, value)
			return
		# 4. Iterate to the end of the linked list at provided index
		prev = node
		while node is not None:
			prev = node
			node = node.next
		# Add a new node at the end of the list with provided key/value
		prev.next = Node(key, value)

	# Find a data value based on key
	# Input:  key - string
	# Output: value stored under "key" or None if not found
	def find(self, key):
		# 1. Compute hash
		index = self.hash(key)
		# 2. Go to first node in list at bucket
		node = self.buckets[index]
		# 3. Traverse the linked list at this node
		while node is not None and node.key != key:
			node = node.next
		# 4. Now, node is the requested key/value pair or None
		if node is None:
			# Not found
			return None
		else:
			# Found - return the data value
			return node.value

if __name__ == '__main__':
  insert_times = []
  search_times = []
  for j in range(10, 31):
    print("{2^"+str(j)+" data}")
    HT = HashTable(j)
    start = time.time()
    for i in range(2**j):
      key = str(random.randint(1, 2**30))
      HT.insert(key, key)
    end = time.time()
    insert_time = round(end - start, 2)
    insert_times.append(insert_time)
    # print("Insert = {:.2f} seconds".format(insert_time))
    print(insert_times)

    open = time.time()
    for i in range(10**5):
      key = str(random.randint(1, 2**30))
      HT.find(key)
    close = time.time()
    search_time = round(close - open, 2)
    search_times.append(search_time)
    # print("Search = {:.2f} seconds".format(search_time))
    print(search_times)
    # print("----------------------------------------")