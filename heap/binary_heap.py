class HeapNode:
    def __init__(self, key: int, element: int):
        self.key = key
        self.element = element


class BinaryHeap:
    def __init__(self, size=1):
        # 存放HeapNode資料的矩陣
        # default constructor會把heap[0]給預留
        # 之後若新增HeapNode, 會從heap[1]開始新增
        if size == 1:
            self.heap = [None]
        else:
            self.heap = [None] * (size+1)

    # private method
    def __swap(self, p1: HeapNode, p2: HeapNode) -> None:
        p1, p2 = p2, p1

    def __findPosition(self, node: int) -> int:
        idx = 0
        for i in range(1, len(self.heap)):
            if self.heap[i].element == node:
                idx = i

        return idx

    def __getParentPosition(self, node: int) -> int:
        return node // 2

    # public method

    def isEmptyHeap(self) -> bool:
        return len(self.heap) <= 1

    # Min-Priority Queue

    def minHeapify(self, node: int, length: int) -> None:
        left = 2 * node  # 取得left child
        right = 2 * node + 1  # 取得right child
        smallest = None  # smallest用來記錄包含root與child, 三者之中Key最小的node

        if left <= length and self.heap[left].key < self.heap[node].key:
            smallest = left
        else:
            smallest = node

        if right <= length and self.heap[right].key < self.heap[smallest].key:
            smallest = right

        if smallest != node:  # 如果目前node的Key不是三者中的最小
            # 就調換node與三者中Key最小的node之位置
            # self.__swap(self.heap[smallest], self.heap[node])
            self.heap[node], self.heap[smallest] =\
                self.heap[smallest], self.heap[node]
            self.minHeapify(smallest, length)  # 調整新的subtree成Min Heap

    def buildMinHeap(self, array: list[int]) -> None:
        # 將array[]的資料放進 heap之矩陣中, 並預留 heap[0] 不做使用
        for i in range(len(array)):
            # self.heap[i + 1].element = i  # 　array[]的idx視為element
            # self.heap[i + 1].key = array[i]  # 把array[]的數值視為key
            self.heap[i + 1] = HeapNode(array[i], i)

        for i in range((len(self.heap)-1) // 2, 0, -1):
            # length要減一, 因為heap從從1開始存放資料
            self.minHeapify(i, len(self.heap) - 1)

    def decreaseKey(self, node: int, newKey: int) -> None:
        index_node = self.__findPosition(node)  # 找到node所在的位置index

        if newKey > self.heap[index_node].key:  # 如果不是把node的Key下修, 便終止此函式
            print('new key larger than current key\n')
            return

        # 更新node之Key後, 需要檢查是否新的subtree滿足Min Heap
        self.heap[index_node].key = newKey

        while index_node > 1 and self.heap[self.__getParentPosition(index_node)].key > self.heap[index_node].key:
            # self.__swap(self.heap[index_node],
            #            self.heap[self.__getParentPosition(index_node)])
            self.heap[index_node], self.heap[self.__getParentPosition(index_node)] =\
                self.heap[self.__getParentPosition(
                    index_node)], self.heap[index_node]
            index_node = self.__getParentPosition(index_node)

    def minHeapInsert(self, node: int, key: int) -> None:
        self.heap.append(HeapNode(key, node))  # 在heap[]尾巴新增一個node
        self.decreaseKey(node, key)

    def minimum(self) -> int:  # 回傳vertex的位置index
        return self.heap[1].element

    def extractMin(self) -> int:  # 回傳vertex的位置index
        if self.isEmptyHeap():
            print("error: heap is empty!\n")
            exit(-1)

        # 此時heap的第一個node具有最小key值  便以min記錄其element, 最後回傳min
        min = self.heap[1].element

        # delete the first element/vertex
        self.heap[1] = self.heap[len(self.heap) - 1]  # 把最後一個element放到第一個位置,
        self.heap.pop()  # 再刪除最後一個element
        self.minHeapify(1, len(self.heap) - 1)  # 目前, heap[1]具有最大Key, 需要進行調整

        return min  # 回傳heap中具有最小key的element

    def display(self) -> None:
        for i in range(1, len(self.heap)):
            print("(id={0}, e={1}, k={2})".format(
                i,
                self.heap[i].element,
                self.heap[i].key
            ))
        print()

    # def HeapSort()

    # Max-Priority Queue


def main():
    binaryHeap = BinaryHeap()
    binaryHeap.minHeapInsert(1, 1)  # A, 1
    binaryHeap.minHeapInsert(2, 2)  # B, 2
    binaryHeap.minHeapInsert(3, 3)  # C, 3
    binaryHeap.display()

    binaryHeap.minHeapInsert(4, 4)  # D, 4
    binaryHeap.minHeapInsert(5, 5)  # E, 5
    binaryHeap.minHeapInsert(6, 6)  # F, 6
    binaryHeap.display()

    ######################################

    distance = [2, 1, 3, 4, 6, 5, 7]
    minQueue = BinaryHeap(len(distance))
    minQueue.buildMinHeap(distance)
    minQueue.display()

    while not minQueue.isEmptyHeap():
        u = minQueue.extractMin()
        print("current heap min: {0}".format(u))
        minQueue.display()


if __name__ == "__main__":
    main()
