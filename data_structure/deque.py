class Deque:
    def __init__(self):
        self.s = []
    def addFront(self, item):
        self.s.append(item)
    def addRear(self, item):
        self.s.insert(0, item)
    def removeFront(self):
        self.s.pop()
    def removeRear(self):
        self.s.pop(0)
    def isEmpty(self):
        return len(self.s) == 0
    def siez(self):
        return len(self.s)