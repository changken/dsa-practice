class MyQueue:
    def __init__(self):
        self.data = [None] * 11  # 會犧牲一個空間
        self.front = 0
        self.rear = 0

    def size(self):
        # 如果後端大於前端，則回傳後端減前端
        if self.front < self.rear:
            return self.rear - self.front
        else:
            # 如果後端小於前端，則回傳陣列長度減前端加後端
            return len(self.data) - (self.front - self.rear)

    def isEmpty(self):
        # 如果前端等於後端，則回傳True
        return self.front == self.rear

    def isFull(self):
        # 如果後端加一除以陣列長度等於前端，則回傳True
        return (self.rear + 1) % len(self.data) == self.front

    def enqueue(self, item):
        if self.isFull():
            raise Exception("Queue is full")

        self.rear = (self.rear + 1) % len(self.data)
        self.data[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")

        res = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        return res

    def getFront(self):
        if self.isEmpty():
            raise Exception("Queue is empty")

        return self.data[(self.front + 1) % len(self.data)]  # 會先加一

    def getRear(self):
        if self.isEmpty():
            raise Exception("Queue is empty")

        return self.data[self.rear]  # 直接接最後一個


if __name__ == '__main__':
    queue = MyQueue()
    queue.enqueue("幹")
    queue.enqueue("你")
    queue.enqueue("娘")
    queue.enqueue("!")
    queue.enqueue("操")
    queue.enqueue("你")
    queue.enqueue("媽")
    queue.enqueue("機")
    queue.enqueue("掰")
    queue.enqueue("!")

    print(queue.getFront())
    print(queue.getRear())

    try:
        queue.enqueue("!")  # 這裡會拋出例外
    except Exception as e:
        print("error!!!")

    assert queue.size() == 10

    queue.dequeue()
    assert queue.size() == 9
    queue.enqueue("104")
    print(queue.getFront())
    print(queue.getRear())

    queue.enqueue("5566")
