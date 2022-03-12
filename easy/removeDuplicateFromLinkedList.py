# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    temp =tail= LinkedList(0)
    cur = linkedList
    while cur :
        while cur.next and cur.value ==cur.next.value:
            cur = cur.next
        tail.next = LinkedList(cur.value)
        tail = tail.next
        cur=cur.next
    return temp.next

