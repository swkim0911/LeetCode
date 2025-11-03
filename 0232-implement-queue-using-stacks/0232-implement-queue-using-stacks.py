class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # stack1은 임시 저장소
    # stack2는 pop 혹은 peek을 위한 저장소
    # b c d
    # c b - peek or pop (연산이 끝나면 stack2는 비워지고 다시 stack1을 채운다)




    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        head_val = self.stack2.pop()
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return head_val


    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        head_val = self.stack2[-1]
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return head_val
        

    def empty(self) -> bool:
        return not self.stack1

# 문제 정의: 두 개의 스택을 이용해서 큐를 구현한다. 단, 스택은 스택의 표준 연산만 할 수 있다.
# 풀이: 하나의 stack(a)에는 push되는 데이터의 임시 저장소가 된다. 
# 그리고 pop이나 peek이 될 때, stack의 가장 먼저 들아건 데이터가 필요하니까 a에서 pop하면서 다른 스택(b)으로 데이터를 push한다. 그러면 a 스택의 가장 뒤에 있는게 b 스택에는 가장 위에 올라오게 되어 First in Frist Out을 구현할 수 있다.


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()