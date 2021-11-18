# Time: 2021/11/11  19:25
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


def infixToPostfix(infix_express:str):
    operator_priority = {'*':3, '/':3, '+':2, '-':2, '(':1, ')':1}
    operators = '+-*/()'
    result = ''
    operator_stack = Stack()
    for token in infix_express:
        if token not in operators:
            result += token
        else:
            if token == '(':
                operator_stack.push(token)
            elif token == ')':
                a = operator_stack.pop()
                while a != '(':
                    result += a
                    a = operator_stack.pop()
            else:
                while not operator_stack.isEmpty() and operator_priority[token] < operator_priority[operator_stack.peek()]:
                    result += operator_stack.pop()
                operator_stack.push(token)

    while not operator_stack.isEmpty():
        result += operator_stack.pop()

    return result


str1 = '( A + B ) * ( C + D )'
str2 = '( A + B ) * C'

print(infixToPostfix(str2.replace(' ','')))
