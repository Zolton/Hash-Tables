class DynamicArray:
    def __init__(self, capacity = 8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity #allocate memory
    
    def insert(self, index, value):
        if self.count >= self.capacity:
            print("Array is full")
            return
        if index > self.count:
            print("Out of range")
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]
        
        self.storage[index] = value
        self.count += 1

my_array = DynamicArray(3)

my_array.insert(0, 5)
my_array.insert(0, 4)
print(my_array.storage)

my_array.insert(2, 3)
print(my_array.storage)

my_array.insert(2, 7)
print(my_array.storage)