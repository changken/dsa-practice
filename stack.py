class Stack:
    def __init__(self, stack_arr=[]):
        self.stack_arr = stack_arr
        self.size = len(stack_arr)

    def __len__(self):
        return self.size

    def push(self, data):
        self.stack_arr.append(data)
        self.size += 1

    def pop(self):
        res = self.peek()
        self.stack_arr = self.stack_arr[:self.size-1]
        self.size -= 1
        return res

    def peek(self):
        return self.stack_arr[self.size-1]


if __name__ == "__main__":
    stack = Stack(["幹", "你", "娘"])
    assert stack.pop() == "娘"
    assert len(stack) == 2
    stack.push("老")
    stack.push("師")
    assert len(stack) == 4
    assert stack.peek() == "師"
    # for i in range(len(stack)):
