from collections import deque
class MyQueue:

    def __init__(self):
        self.de1 = deque([])
        self.de2 = deque([])

    def push(self, x: int) -> None:
        self.de1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.de2.pop()

    def peek(self) -> int:
        if len(self.de2) == 0:
            while len(self.de1) != 0:
                self.de2.append(self.de1.pop())
        return self.de2[-1]

    def empty(self) -> bool:
        return len(self.de1) ==0 and len(self.de2) ==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()