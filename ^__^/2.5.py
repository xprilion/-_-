from LinkedList import LinkedList

# def sumList(a, b):
#     if a.head == None:
#         return b
#     elif b.head == None:
#         return a

#     c = []

#     ta = a.head
#     tb = b.head

#     carry = 0
#     while ta != None and tb != None:
#         s = ta.data + tb.data + carry
#         c.append(s % 10)
#         carry = int(s > 9)
#         ta = ta.next
#         tb = tb.next

#     if ta == None:
#         tx = tb
#     else:
#         tx = ta

#     while tx != None:
#         s = tx.data + carry
#         c.append(s % 10)
#         carry = s - c[-1]
#         tx = tx.next

#     if carry != 0:
#         c.append(carry)

#     ll = LinkedList()
#     ll.pushList(c)

#     return ll

def sumList(a, b):
    if a.head == None:
        return b
    elif b.head == None:
        return a

    c = LinkedList()

    ta = a.head
    tb = b.head

    carry = 0
    while ta or tb:
        s = 0

        if ta:
            s += ta.data
            ta = ta.next

        if tb:
            s += tb.data
            tb = tb.next

        if carry:
            s += carry

        c.push(s % 10)
        carry = int(s > 9)


    if carry != 0:
        c.push(carry)

    return c


a = LinkedList()
b = LinkedList()

a.pushList([9, 2, 3])
b.pushList([9, 2, 9])

a.display()
b.display()

c = sumList(a, b)

c.display()