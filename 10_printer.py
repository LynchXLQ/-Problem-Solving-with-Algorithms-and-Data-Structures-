# Time: 2021/11/19  23:18
import random
from queue import Queue


class Printer:
    def __init__(self, ppm):
        self.printRate = ppm
        self.currentTask = None
        self.remainTime = 0

    def startNextTask(self, task):
        self.currentTask = task
        self.remainTime = (task.getPages()/self.printRate)*60

    def isBusy(self):
        if self.currentTask == None:
            return False
        else:
            return True

    def tick(self):
        if self.currentTask:
            self.remainTime -= 1
            if self.remainTime <= 0:
                self.currentTask = None




class Task:
    def __init__(self, timestamp):
        self.startTime = timestamp
        self.pages = random.randint(1,20)

    def getPages(self):
        return self.pages

    def getStartTime(self):
        return self.startTime

    def getWaitTime(self, currenttime):
        return currenttime - self.startTime



def newTask():
    '''
    find out whether there is a new print task
    '''
    num = random.randint(1,180)
    if num == 180:
        return True
    else:
        return False

def simulation(numseconds, pagesperMinute):
    waitTimeList = []
    printQueue = Queue()
    printer = Printer(pagesperMinute)

    for currentSecond in range(numseconds):

        if newTask():
            task = Task(currentSecond)
            printQueue.put(task)
        if not printQueue.empty() and not printer.isBusy():
            nextTask = printQueue.get()
            waitTimeList.append(nextTask.getWaitTime(currentSecond))
            printer.startNextTask(nextTask)
        printer.tick()

    averageWaitTime = sum(waitTimeList)/len(waitTimeList)
    print(f'Average waiting time: {averageWaitTime:.3f} secs, {printQueue.qsize()} tasks remain')




if __name__ == '__main__':
    for i in range(10):
        simulation(3600, 5)


















