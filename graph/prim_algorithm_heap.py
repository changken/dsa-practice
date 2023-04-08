class HeapNode:
    def __init__(self, key: int, element: int):
        self.key = key
        self.element = element


class BinaryHeap:
    def __init__(self, n: int = 1) -> None:
        # 主要存放vertex及其distance的vector
        self.heap: list[HeapNode] = [None for _ in range(n+1)]

    def _FindPosition(self, node: int) -> int:
        idx = 0
        for i in range(1, len(self.heap)):
            if self.heap[i].element == node:
                idx = i
                return idx

        return idx

    def _GetParentPosition(self, node: int) -> int:
        return node // 2

    # Min-Priority Queue

    def MinHeapify(self, node: int, length: int) -> None:
        left = 2 * node  # 取得left child
        right = 2 * node + 1  # 取得right child
        smallest = node  # smallest用來記錄包含root與child, 三者之中Key最小的node

        if left <= length and self.heap[left].key < self.heap[smallest].key:
            smallest = left

        if right <= length and self.heap[right].key < self.heap[smallest].key:
            smallest = right

        if smallest != node:  # 如果目前node的Key不是三者中的最小
            # 就調換node與三者中Key最小的node之位置
            self.heap[node], self.heap[smallest] = self.heap[smallest], self.heap[node]
            # 調整新的subtree成Min Heap
            self.MinHeapify(smallest, length)

    def BuildMinHeap(self, array: list[int]) -> None:
        # 將array[]的資料放進 heap之矩陣中, 並預留 heap[0] 不做使用
        for i in range(len(array)):
            self.heap[i+1].element = i  # 把array[]的idx視為element
            self.heap[i+1].key = array[i]  # 把array[]的數值視為key

        for i in range(len(array)//2, 0, -1):
            self.MinHeapify(i, len(array)-1)  # length要減一, 因為heap從從1開始存放資料

    def DecreaseKey(self, node: int, new_key: int) -> None:
        index_node = self._FindPosition(node)  # 找到node所在的位置index

        # 如果不是把node的Key下修, 便終止此函式
        if new_key > self.heap[index_node].key:
            print("new key is not smaller than current key\n")
            return

        self.heap[index_node].key = new_key  # 更新node之Key後,
        # 需要檢查是否新的subtree滿足Min Heap

        while index_node > 1 and \
                self.heap[self._GetParentPosition(index_node)].key > self.heap[index_node].key:
            self.heap[index_node], self.heap[self._GetParentPosition(index_node)] = \
                self.heap[self._GetParentPosition(
                    index_node)], self.heap[index_node]
            index_node = self._GetParentPosition(index_node)

    def MinHeapInsert(self, node: int, key: int) -> None:
        self.heap.append(HeapNode(key, node))  # 將新的node加入heap的最後一個位置
        self.DecreaseKey(node, key)  # 並將新的node的Key下修

    # 回傳heap[1]並調整Heap
    def ExtractMin(self) -> int:
        pass


def main():
    pass


if __name__ == "__main__":
    main()
