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
        pass

    def __findPosition(self, node: int) -> int:
        pass

    def __getParentPosition(self, node: int) -> int:
        return node // 2

    # public method

    def isEmptyHeap(self) -> bool:
        return len(self.heap) < 1

    # Min-Priority Queue

    def minHeapify(self, node: int, length: int) -> None:
        left = 2 * node  # 取得left child
        right = 2 * node + 1  # 取得right child
        smallest = None  # smallest用來記錄包含root與child, 三者之中Key最小的node

        if left <= length and self.heap[left].key < self.heap[node].key:
            smallest = left
        else:
            smallest = node

        if right <= length and self.heap[right].key < self.heap[node].key:
            smallest = right

        if smallest != node: # 如果目前node的Key不是三者中的最小 
            self.__swap(self.heap[smallest], self.heap[node]) # 就調換node與三者中Key最小的node之位置
            self.minHeapify(smallest, length) # 調整新的subtree成Min Heap

    def buildMinHeap(self, array: list[int]) -> None:
        # 將array[]的資料放進 heap之矩陣中, 並預留 heap[0] 不做使用
        for i in range(len(array)):
            self.heap[i + 1].element = i #　array[]的idx視為element
            self.heap[i + 1].key = array[i] # 把array[]的數值視為key
        
        for i in range(len(self.heap) // 2, 0, -1):
            self.minHeapify(i, len(self.heap) - 1) # length要減一, 因為heap從從1開始存放資料

    def decreaseKey(self, node: int, newKey: int) -> None:
        pass

    def minHeapInsert(self, node: int, key: int) -> None:
        pass

    def minimum(self) -> int:  # 回傳vertex的位置index
        pass

    def extractMin(self) -> int:  # 回傳vertex的位置index
        pass

    # def HeapSort()

    # Max-Priority Queue


def main():
    pass


if __name__ == "__main__":
    main()
