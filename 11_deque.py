# Time: 2021/11/21  22:25

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addLeft(self, item):
        return self.items.insert(0, item)

    def addRight(self, item):
        return self.items.append(item)

    def removeLeft(self):
        return self.items.pop()

    def removeRight(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
