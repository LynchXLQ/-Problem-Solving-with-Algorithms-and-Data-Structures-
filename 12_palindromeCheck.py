# Time: 2021/11/21  22:55
from collections import deque

def palCheck(string):
    chardeque = deque()
    for char in string:
        chardeque.append(char)
    Equal = True
    while len(chardeque) > 1 and Equal:
        left = chardeque.popleft()
        right = chardeque.pop()
        if left != right:
            Equal = False
    return Equal

print(palCheck('ba'))
