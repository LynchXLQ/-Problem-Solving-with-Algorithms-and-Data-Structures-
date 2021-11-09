class Stack:
    def __init__(self):
        self.items = []   # list 尾部作为栈顶

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)  # O(1)

    def pop(self):
        return self.items.pop()   # O(1)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)