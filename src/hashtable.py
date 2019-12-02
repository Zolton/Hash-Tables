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
        
        # Hash the key, figure where in the array it should go
        indexLocation = self._hash_mod(key)
        print("IndexLocation: ", indexLocation)

        # If hashTable is full, make it bigger to fit
        if self.count >= self.capacity:
            print("Hash Table is too small")
            return
            # self.resize()
            #self.insert(key, value)

        # If for whatever reason the function tries to insert into
        # a location outside the current hash table
        if indexLocation > self.count:
            print("Out of range")
            return
        # With the hashed key as the indexLocation, insert the value
        for i in range(self.count, indexLocation, -1):
            self.storage[i] = self.storage[i-1]
        self.storage[indexLocation] = value
        self.count += 1

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        indexLocation = self._hash_mod(key)
        for i in range (indexLocation, self.count -1, 1):
            self.storage[i] = self.storage[i+1]
        self.count -= 1
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        indexLocation = self._hash_mod(key)
        return self.storage[indexLocation]


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.storage *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)
    print("storage: ", ht.storage)
    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
