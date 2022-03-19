class FreqStack:

    def __init__(self):
        self.stack=[]
        self.hashTable = {}
        self.maxOccur = 0 

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.hashTable[val] = self.hashTable.get(val,0)+1
        
        if self.hashTable[val] > self.maxOccur:
            self.maxOccur = self.hashTable[val]

    def pop(self) -> int:
        idx = len(self.stack)-1
        
        for val in self.stack[::-1]:
            
            if self.hashTable[val]  == self.maxOccur:
                self.hashTable[val] -=1
                
                self.maxOccur = max(self.hashTable.values())
                
                return self.stack.pop(idx)

            idx -=1


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()