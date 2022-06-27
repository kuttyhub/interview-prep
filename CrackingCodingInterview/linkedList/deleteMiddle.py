from LinkedList import LinkedList

def deleteMiddle(head):
    slow = fast =head
    prev =None
    print(head)
    while fast.next:
        fast = fast.next.next
        prev= slow 
        slow = slow.next

    #deleting
    prev.next =prev.next.next
    print(head) 


ll = LinkedList() 
ll.populateList([1,2,3,4,2,3,4])

deleteMiddle(ll.head)