from LinkedList import LinkedList

def kthLast(ll, k):
    if k > ll.count:
        return None
    else:
        runner = cursor = ll.head

        for i in range(k):
            runner = runner.next

        while runner.next != None:
            cursor = cursor.next
            runner = runner.next

        return cursor.data


ll = LinkedList()

ll.pushList([12, 1, 123, 12, 4 ,5, 6, 2, 4, 6, 4, 9, 4, 9, 8,8, 1])

ll.display()

x = kthLast(ll, 0)

print(x)