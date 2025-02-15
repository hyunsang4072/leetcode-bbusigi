class MinStack: # pretty simple design question

    def __init__(self):
        # since when we pop from our stack, it's hard to keep track of
        # what's our new minVal, we use extra memory to make it work
        self.arr = [] # to keep track of multiple mininum vals at index i
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val, self.arr[-1]) if self.arr else val
        self.arr.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.arr.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.arr[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()