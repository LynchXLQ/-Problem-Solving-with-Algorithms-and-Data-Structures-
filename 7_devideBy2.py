# Time: 2021/11/11  12:39
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



def devideBy2_1(dec_num: int):
    '''
    Not use stack
    '''
    bin_num = []
    while True:
        result = dec_num // 2
        remainder = dec_num % 2
        dec_num = result
        print(f'remainder:{remainder}')
        bin_num.append(remainder)
        if dec_num == 0:
            return bin_num[::-1]

def devideBy2_2(dec_num: int):
    '''
    Use stack
    '''
    rem_stack = Stack()
    while dec_num > 0:
        rem_stack.push(dec_num % 2)
        dec_num = dec_num // 2
        print(f'decimal number: {dec_num}')
    bin_num = ''
    while not rem_stack.isEmpty():
        bin_num += str(rem_stack.pop())
    return bin_num

def baseConverter(dec_num: int, base: int):
    digits = '0123456789ABCDEF'
    rem_stack = Stack()
    while dec_num > 0:
        rem_stack.push(dec_num % base)
        dec_num = dec_num // base
        print(f'decimal number: {dec_num}, base: {base}')
    result = ''
    while not rem_stack.isEmpty():
        result += digits[rem_stack.pop()]
    return result







# print(devideBy2_1(233))
# print(devideBy2_2(233))
print(baseConverter(dec_num=233, base=10))