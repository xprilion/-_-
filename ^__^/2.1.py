from LinkedList import LinkedList

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
