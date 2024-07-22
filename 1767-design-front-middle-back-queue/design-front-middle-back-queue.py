class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = deque()
        self.queue2 = deque()


    def pushFront(self, val: int) -> None:
        self.queue.appendleft(val)


    def pushMiddle(self, val: int) -> None:
        if len(self.queue)%2==0:
            for i in range(len(self.queue)//2):
                self.queue2.append(self.queue.pop())
            self.queue.append(val)
            for i in range(len(self.queue2)):
                self.queue.append(self.queue2.pop())
        else:
            for i in range((len(self.queue)//2)+1):
                self.queue2.append(self.queue.pop())
            self.queue.append(val)
            for i in range(len(self.queue2)):
                self.queue.append(self.queue2.pop())


    def pushBack(self, val: int) -> None:
        self.queue.append(val)



    def popFront(self) -> int:
        if len(self.queue)!=0:
            return self.queue.popleft()
        else:
            return -1
        

    def popMiddle(self) -> int:
        a = len(self.queue)
        if a==0:
            return -1
        if a%2==0:
            ans = self.queue[(a//2)-1]
            for i in range(a//2):
                self.queue2.append(self.queue.pop())
            self.queue.pop()
            for i in range(len(self.queue2)):
                self.queue.append(self.queue2.pop())
            return ans

        else:
            ans = self.queue[(a//2)]
            for i in range(a//2):
                self.queue2.append(self.queue.pop())
            self.queue.pop()
            for i in range(len(self.queue2)):
                self.queue.append(self.queue2.pop())
            return ans


    def popBack(self) -> int:
        if len(self.queue) != 0:
            return self.queue.pop()
        else:
            return -1
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()