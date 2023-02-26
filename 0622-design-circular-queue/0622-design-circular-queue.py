class MyCircularQueue:

    def __init__(self, k: int):
        self.c_queue = [None] * k
        self.max_len = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.c_queue[self.rear] is None:
            self.c_queue[self.rear] = value
            self.rear = (self.rear + 1) % self.max_len
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.c_queue[self.front] is None:
            return False
        else:
            self.c_queue[self.front] = None
            self.front = (self.front + 1) % self.max_len
            return True

    def Front(self) -> int:
        return -1 if self.c_queue[self.front] is None else self.c_queue[self.front]

    def Rear(self) -> int:
        return -1 if self.c_queue[self.rear - 1] is None else self.c_queue[self.rear -1]

    def isEmpty(self) -> bool:
        return self.rear == self.front and self.c_queue[self.front] is None

    def isFull(self) -> bool:
        return self.rear == self.front and self.c_queue[self.front] is not None
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()