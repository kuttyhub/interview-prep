from LinkedList import LinkedList

def checkPalindrome(head):
    slow = fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if slow.value != stack.pop():
            return False
        slow = slow.next
    return True


ll = LinkedList() 
ll.populateList([1,2,3,4,3,2,1])
print(checkPalindrome(ll.head))