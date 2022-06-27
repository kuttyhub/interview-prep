from tkinter import NO
from LinkedList import LinkedList

def checkIntersection(head1, head2):
    t1,s1 = getTailAndSize(head1)
    t2,s2 = getTailAndSize(head2)
    
    if t1 != t2:
        return None
    
    k = s1 - s2

    if k < 0:
        head2 = chopKNodes(abs(k),head2)
    elif k > 0:
        head1 = chopKNodes(k,head1)
    
    while (head1 != head2):
        head1 = head1.next
        head2 = head2.next
    
    return head1

def getTailAndSize(head):
    curr = head
    size = 1
    while curr.next:
        size += 1
        curr = curr.next
    return curr,size

def chopKNodes(k,head):
    curr = head
    while k > 0 and curr:
        curr = curr.next
        k -= 1
    return curr

def intersectList(k,head1,head2):
    curr = head1
    while k>0:
        k-=1
        curr = curr.next
    head2.next = curr


ll = LinkedList()
ll.populateList([1,2,3,4,5,6,7,8,9,10])
l2 = LinkedList()
l2.populateList([0])

intersectList(4,ll.head,l2.head)

print(checkIntersection(ll.head, l2.head))