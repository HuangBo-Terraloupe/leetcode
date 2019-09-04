class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    def getdata(self):
        return self.data
    def getnext(self):
        return self.next
    def setdata(self, newdata):
        self.data = newdata
    def setnext(self, newnext):
        self.next = newnext

class UnorderedList:
    def	__init__(self):
        self.head =	None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp

    def listprint(self):
        print_item = self.head
        while print_item is not None:
            print(print_item.getdata())
            print_item = print_item.getnext()

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getnext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getdata() == item:
                found = True
            else:
                current = current.getnext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current is None:
                return
            if current.getdata() == item:
                found = True
            else:
                previous = current
                current = current.getnext()
        if previous is None:
            self.head = current
        else:
            previous.setnext(current.getnext())

class OrderedList:
    def	__init__(self):
        self.head =	None

    def is_empty(self):
        return self.head == None

    def listprint(self):
        print_item = self.head
        while print_item is not None:
            print(print_item.getdata())
            print_item = print_item.getnext()

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getnext()
        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while (current is not None) and (not found) and (not stop):
            if current.getdata() == item:
                found = True
            else:
                if current.getdata() > item:
                    stop = True
                else:
                    current = current.getnext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        # find the adding position
        while current != None and not stop:
            if current.getdata() > item:
                stop = True
            else:
                previous = current
                current = current.getnext()

        # add item
        temp = Node(item)
        if previous is None:
            temp.setnext(self.head)
            self.head = temp
        else:
            temp.setnext(current)
            previous.setnext(temp)