class MinStack:

    def __init__(self):
        self.list = []

    def push(self, val: int) -> None:
        self.list.append(val)
        

    def pop(self) -> None:
        self.list.pop()

    def top(self) -> int:
        # t1 = self.list.pop()
        # return t1 
        return self.list[-1]

    def getMin(self) -> int:
        return min(self.list)  
        
