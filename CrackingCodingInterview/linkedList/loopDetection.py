from LinkedList import LinkedList



def checkLoop(head):
    slow = fast = head

    while fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break

    if fast is None or fast.next is None:
        return False

    # finding starting collision point
    slow =head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return True

ll = LinkedList() 
ll.populateList([1,2,3,4,2,3,4])
print(checkLoop(ll.head))