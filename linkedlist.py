class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    # 從頭部加入節點
    def add(self, data):
        current_node = SinglyNode(data)

        if self.head is None:
            self.head = current_node
            self.tail = current_node
        else:
            current_node.next = self.head
            self.head = current_node

        self.size += 1

    # 從頭部移除節點
    def remove(self):
        if self.head is None:
            raise ValueError("List is empty")
        else:
            tmp = self.head
            self.head = self.head.next
            del tmp
            self.size -= 1

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next


class SinglyNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


if __name__ == "__main__":

    test_arr = ["nigger", "bitch", "lol"]

    lst = SinglyLinkedList()
    lst.add("nigger")
    lst.add("bitch")
    lst.add("lol")

    for item in lst:
        assert item in test_arr

    lst.remove()
    assert len(lst) == 2

    lst.add("幹你老師")
    assert len(lst) == 3
    for item in lst:
        if item == "幹你老師":
            assert True
