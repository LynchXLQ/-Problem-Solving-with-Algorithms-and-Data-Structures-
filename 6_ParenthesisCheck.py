
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


def parCheck(symbolString):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
        index += 1
    return balance and s.isEmpty()

print(parCheck(''))