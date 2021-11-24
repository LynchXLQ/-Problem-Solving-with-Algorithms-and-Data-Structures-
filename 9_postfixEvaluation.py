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


def postfixEval(postfixExpressian: str):
    operators = '+-*/()'
    number_stack = Stack()
    for token in postfixExpressian:
        if token not in operators:
            number_stack.push(token)
        else:
            operand_right = number_stack.pop()
            operand_left = number_stack.pop()
            result = doMath(token, operand_right, operand_left)
            number_stack.push(result)
    return number_stack.pop()

def doMath(operator, operand_right, operand_left):
    if operator == '+':
        return operand_left + operand_right
    elif operator == '-':
        return operand_left - operand_right
    elif operator == '*':
        return operand_left * operand_right
    elif  operator == '/':
        return operand_left / operand_right
