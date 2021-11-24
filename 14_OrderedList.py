# Time: 2021/11/22  22:32
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


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def length(self):
        cnt = 0
        current = self.head
        while current != None:
            cnt += 1
            current = current.getNext()
        return cnt

    def search(self, item):
        current = self.head
        find = False
        stop = False
        while not find and not stop and current != None:
            if current.getData() == item:
                find = True
            elif current.getData() > item:
                stop = True
            elif current.getData() < item:
                current.getNext()

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                current = current.getNext()
                previous = current
        temp = Node(item)
        if previous != None:
            temp.setNext(current)
            previous.setNext(temp)
        else:
            temp.setNext(self.head)
            self.head = temp








