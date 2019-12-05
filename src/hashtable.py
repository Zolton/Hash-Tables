# '''
# Linked List hash table key/value pair
# '''

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
         # Use pythons built-in hash function
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

   

    # def _hash_djb2(self, key):
    #     '''
    #     Hash an arbitrary key using DJB2 hash

    #     OPTIONAL STRETCH: Research and implement DJB2
    #     '''
    #     pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        if self.count <= self.capacity:
            self.resize()
        # Hash the key, figure where in the array it should go
        indexLocation = self._hash_mod(key)
        current_node = self.storage[indexLocation]
        if current_node is None:
            self.storage[indexLocation] = LinkedPair(key, value)
            self.count += 1
            return
        if current_node.next is not None:
            while current_node.next is not None:
                if current_node.next is None:
                    current_node.next = LinkedPair(key, value)
                    self.count += 1
                    return
                else:
                    current_node.next = current_node.next.next
        else:
            current_node.next = LinkedPair(key, value)
            self.count += 1


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        indexLocation = self._hash_mod(key)
        if self.storage[indexLocation] is None:
            print("Invalid key")
            return
        self.storage[indexLocation] = None
        
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        indexLocation = self._hash_mod(key)
        current_node = self.storage[indexLocation]
        # if current_node.key is None:
        #     print ("Invalid key")
        #     return
        if current_node is None:
            return None
        if current_node.key is key:
            #print("got it on first try")
            return current_node.value
        else:
            while current_node.next is not None:
                if current_node.next.key is key:
                    #print("found it in the list")
                    return current_node.next.value
                else:
                    #print("moving on")
                    current_node = current_node.next
            return current_node.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in self.storage:
            if i is not None:
                newIndex = self._hash_mod(i.key)
                new_storage[newIndex] = LinkedPair(i.key, i.value)
        self.storage = new_storage

# hashT = HashTable(2)
# print(hashT.storage)
# hashT.insert("gabba", "haha")
# print(hashT.storage)
# hashT.insert("zylophone", "lol")
# print(hashT.storage)
# print(hashT.storage)
# hashT.insert("gabba222", "haha222")
# print(hashT.storage)
# hashT.insert("zylophone222", "lol222")
# print(hashT.storage)
# print("Key return: ", hashT.retrieve("gabba"))
# print("Key return: ", hashT.retrieve("zylophone"))
# print("Key return: ", hashT.retrieve("gabba222"))
# print("Key return: ", hashT.retrieve("zylophone222"))
# print(hashT.storage)
# hashT.remove("gabba")
# print(hashT.storage)
# hashT.resize()
# print(hashT.storage)
# print("Key return: ", hashT.retrieve("gabba"))
# print("Key return: ", hashT.retrieve("zylophone"))

# if __name__ == "__main__":
#     ht = HashTable(2)
#     print("storage: ", ht.storage)
#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
