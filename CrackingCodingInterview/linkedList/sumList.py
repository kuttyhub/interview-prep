from LinkedList import LinkedList

def sumIt(head1,head2):
    s1,s2 = getString(head1)[::-1],getString(head2)[::-1]
    print(s1,s2)
    result = str(int(s1)+int(s2))
    res = [int(i) for i in result]
    l3 = LinkedList()
    l3.populateList(res)
    print(l3.head)
    

def getString(head):
    s =""
    temp = head
    while temp:
        s += str(temp.value)
        temp = temp.next
    return s

l1 = LinkedList() 
l1.populateList([7,1,6])
l2 = LinkedList() 
l2.populateList([5,9,2])

sumIt(l1.head,l2.head)


