class Hashtable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def set(self, key, value):
        index = self.hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                entry[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                return entry[1]
        return None

    def has(self, key):
        index = self.hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                return True
        return False

    def keys(self):
        keys = []
        for entries in self.table:
            for entry in entries:
                keys.append(entry[0])
        return keys

    def hash(self, key):
        return hash(key) % self.size
