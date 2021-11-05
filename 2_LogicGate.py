# Time: 2021/11/4  22:13

class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):  # 继承类
    def __init__(self, label):
        super().__init__(label)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input('Enter Pin A input for gate' + self.getLabel() + '-->'))

    def getPinB(self):
        return int(input('Enter Pin B input for gate' + self.getLabel() + '-->'))


class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin = None

    def getPin(self):
        return int(input('Enter Pin input for gate' + self.getLabel() + '-->'))


class AndGate(BinaryGate):   # 与门
    def __init__(self, label):
        super().__init__(label)

    def performGateLogic(self):
        pinA = self.getPinA()
        pinB = self.getPinB()
        print(pinA, pinB, type(pinA))
        if pinA == 1 and pinB == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):  # 或门
    def __init__(self, label):
        super().__init__(label)

    def performGateLogic(self):
        pinA = self.getPinA()
        pinB = self.getPinB()
        if pinA == 0 and pinB == 0:
            return 1
        else:
            return 0


class NotGate(UnaryGate):   # 非门
    def __init__(self, label):
        super().__init__(label)

    def  performGateLogic(self):
        pin = self.getPin()
        if pin == 1:
            return 0
        else:
            return 1


g1 = AndGate('G1')
g1.getOutput()






















