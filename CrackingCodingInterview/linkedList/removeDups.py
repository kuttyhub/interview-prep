from LinkedList import LinkedList

def removeDups(head):
    if head is None or head.next is None:
        return
    
    s = set()
    s.add(head.value)
    temp = head

    print("before ->",head)
    
    while temp.next:
        if temp.next.value in s:
            temp.next = temp.next.next
        else:
            s.add(temp.next.value)
            temp =temp.next
    
    print("after -> ",head)



ll = LinkedList() 
head = ll.populateList([1,2,3,4,2,3,4])

removeDups(head)