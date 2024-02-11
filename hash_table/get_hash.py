
# def get_hash(key):
#     h = 0
#     for char in key:
#         h += ord(char)
#     return h % 100

# print(get_hash("march 21"))

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

t = HashTable()
print(t.get_hash("march 28"))
print(t.add("march 28", 30))
print(t.get("march 28"))


