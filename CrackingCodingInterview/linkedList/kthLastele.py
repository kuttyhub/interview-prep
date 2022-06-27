from LinkedList import LinkedList

def kthLastElement(head,k):
    print(head)
    fast = slow = head
    while k != 0:
        fast = fast.next
        k-=1
    while fast:
        fast = fast.next
        slow = slow.next
    
    return slow.value
    

ll = LinkedList() 
head = ll.populateList([1,2,3,4,2,3,4])
print(kthLastElement(head,3))
