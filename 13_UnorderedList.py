# Time: 2021/11/21  23:44

class Node:
    def __init__(self, initialdata):
        self.data = initialdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)  # 第1 步，将新节点的next引用指向当前列表中的第一个节点
        self.head = temp  # 第2 步，修改列表的头节点，使其指向新创建的节点

    def length(self):
        current = self.head
        cnt = 0
        while current != None:
            cnt += 1
            current = current.getNext()
        return cnt

    def search(self, item):
        find = False
        current = self.head
        while current != None and not find:
            if current.getData() == item:
                find = True
            else:
                current = current.getNext()
        return find

    def remove(self, item):
        current = self.head
        previous = None
        find = False
        while not find:
            if current.getData() == item:
                find = True
            else:
                current = current.getNext()
                previous = current
        if previous == Node:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())





























