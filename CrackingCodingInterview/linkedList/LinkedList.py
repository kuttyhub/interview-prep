class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def populateList(self,arr):
        temp= self.head
        for i in arr:
            if temp is None:        
                self.head = temp = Node(i)
            else:
                temp.next = Node(i)
                temp = temp.next
        return self.head
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        return f" {self.value}  -> {self.next}"