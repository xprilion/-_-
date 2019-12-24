class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def atStart(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.count += 1

    def atEnd(self, data):
        self.atIndex(data, self.count)

    def push(self, data):
        self.atEnd(data)

    def pushList(self, lst):
        _ = [self.push(x) for x in lst]

    def atIndex(self, data, index):
        if index == 0:
            self.atStart(data)
        else:
            newNode = Node(data)
            i = 0
            tmp = self.head
            while i < index -1:
                i += 1
                tmp = tmp.next
            newNode.next = tmp.next
            tmp.next = newNode
            self.count += 1

    def remove(self, index):
        if index < self.count and self.count > 0:
            if index == 0:
                tmp = self.head
                self.head = tmp.next
                del tmp
                self.count -= 1
            else:
                i = 0
                tmp = self.head
                while i < index - 1:
                    i += 1
                    tmp = tmp.next

                removeNode = tmp.next
                tmp.next = tmp.next.next
                del removeNode
                self.count -= 1
        else:
            print("Illegal operation")

    def pop(self):
        tmp = self.head
        while tmp.next != None:
            tmp = tmp.next
        self.remove(self.count-1)
        return tmp

    def display(self):
        tmp = self.head
        while tmp != None:
            print(tmp.data, end=", ")
            tmp = tmp.next

        print("")
        
def removeDups(ll):
    tmp = ll.head
    visited = []

    while tmp.next != None:
        if tmp.next.data in visited:
            tmp.next = tmp.next.next
        else:
            visited.append(tmp.next.data)
            tmp = tmp.next

ll = LinkedList()

ll.pushList([12, 1, 123, 12, 4 ,5, 6, 2, 4, 6, 4, 9, 4, 9, 8,8, 1])

ll.display()

removeDups(ll)

ll.display()
