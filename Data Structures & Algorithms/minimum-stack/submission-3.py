class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_val:
            self.min_val.append(val)

        elif val <= self.min_val[-1]:
            self.min_val.append(val)
            

    def pop(self) -> None:
        remove = self.stack.pop()
        if self.min_val and self.min_val[-1] == remove:
            self.min_val.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
        
