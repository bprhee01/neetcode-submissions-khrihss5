

class Node:
    def __init__(self,val,minVal):
        self.val = val
        self.minVal = minVal

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minVal = val
        if not self.stack:
            minVal = val
        else:
            minVal = min(val, self.stack[-1].minVal)

        newNode = Node(val,minVal)
        self.stack.append(newNode)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].minVal
        
