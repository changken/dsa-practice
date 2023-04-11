import math
from collections import deque

############### MinHeap ###############


class HeapNode:
    def __init__(self, key: int, element: int):
        self.key = key
        self.element = element


class BinaryHeap:
    def __init__(self, n: int = 1) -> None:
        # 主要存放vertex及其distance的vector
        if n == 1:
            self.heap = [None]
        else:
            self.heap = [None] * (n + 1)
        # print("self.heap={0}".format(self.heap))

    def __swap(self, p1: HeapNode, p2: HeapNode) -> None:
        p1, p2 = p2, p1

    def __FindPosition(self, node: int) -> int:
        idx = 0
        for i in range(1, len(self.heap)):
            # 如果找到node，就回傳其位置
            if self.heap[i].element == node:
                idx = i

        return idx

    def __GetParentPosition(self, node: int) -> int:
        # 回傳node的parent的位置
        return node // 2

    # Min-Priority Queue

    def MinHeapify(self, node: int, length: int) -> None:
        left = 2 * node  # 取得left child
        right = 2 * node + 1  # 取得right child
        smallest = None  # smallest用來記錄包含root與child, 三者之中Key最小的node

        # 如果left child的key小於root的key, smallest就記錄left child的位置
        if left <= length and self.heap[left].key < self.heap[node].key:
            smallest = left
        else:
            smallest = node

        # 如果right child的key小於root的key, smallest就記錄right child的位置
        if right <= length and self.heap[right].key < self.heap[smallest].key:
            smallest = right

        print("node={0}, smallest={1}, left={2}, right={3}, length={4}, len_heap={5}".format(
            node, smallest, left, right, length, len(self.heap)))

        if smallest != node:  # 如果目前node的Key不是三者中的最小
            # 就調換node與三者中Key最小的node之位置
            #self.__swap(self.heap[smallest], self.heap[node])
            self.heap[smallest], self.heap[node] = \
                self.heap[node], self.heap[smallest]
            # 調整新的subtree成Min Heap
            self.MinHeapify(smallest, length)

    def BuildMinHeap(self, array: list[int]) -> None:
        # 將array[]的資料放進 heap之矩陣中, 並預留 heap[0] 不做使用
        for i in range(len(array)):
            # self.heap[i+1].element = i  # 把array[]的idx視為element
            # self.heap[i+1].key = array[i]  # 把array[]的數值視為key
            self.heap[i + 1] = HeapNode(array[i], i)

        # 從最後一個具有child的parent node開始到root, 依序調整成Min Heap
        for i in range((len(self.heap)-1) // 2, 0, -1):
            # length要減一, 因為heap從1開始存放資料
            self.MinHeapify(i, len(self.heap) - 1)

    def DecreaseKey(self, node: int, new_key: int) -> None:
        index_node = self.__FindPosition(node)  # 找到node所在的位置index

        print(f"node={node}, index_node={index_node}")

        # 如果找不到index_node(default=0)
        if index_node == 0:
            print("this node is not found in this binary heap!\n")
            return

        # 如果不是把node的Key下修, 便終止此函式
        if new_key > self.heap[index_node].key:
            print("new key is not smaller than current key\n")
            return

        self.heap[index_node].key = new_key  # 更新node之Key後,

        # 需要檢查是否新的subtree滿足Min Heap的性質
        # index_node是否大於1, 且parent的key是否大於child的key
        while index_node > 1 and \
                self.heap[self.__GetParentPosition(index_node)].key > self.heap[index_node].key:
            # 與parent交換位置
            # self.__swap(self.heap[index_node],
            #           self.heap[self.__GetParentPosition(index_node)])
            self.heap[index_node], self.heap[self.__GetParentPosition(index_node)] = \
                self.heap[self.__GetParentPosition(
                    index_node)], self.heap[index_node]
            # 取得下一個parent的位置
            index_node = self.__GetParentPosition(index_node)

    def MinHeapInsert(self, node: int, key: int) -> None:
        self.heap.append(HeapNode(key, node))  # 將新的node加入heap的最後一個位置
        self.DecreaseKey(node, key)  # 並將新的node的Key下修，進而調整成Min Heap

    # 回傳heap[1]並調整Heap
    def ExtractMin(self) -> int:
        # 如果heap是空的, 便終止此函式
        if self.IsHeapEmpty():
            print("error: heap is empty\n")
            exit(-1)

        min = self.heap[1].element  # 此時heap的第一個node具有最小key值
        # 便以min記錄其element, 最後回傳min
        # delete the first element/vertex
        self.heap[1] = self.heap[len(self.heap)-1]  # 把最後一個element放到第一個位置,
        self.heap.pop()  # 再刪除最後一個element
        self.MinHeapify(1, len(self.heap) - 1)  # 目前, heap[1]具有最大Key, 需要進行調整

        return min  # 回傳heap中具有最小key的element

    # 回傳heap[1]
    def Minimum(self) -> int:
        return self.heap[1].element

    def IsHeapEmpty(self) -> bool:
        return len(self.heap) <= 1

    def display(self) -> None:
        for i in range(1, len(self.heap)):
            print("(i={0}, e={1}, k={2})".format(
                i,
                self.heap[i].element,
                self.heap[i].key
            ))
        print()

############### Prim's Algorithm ###############


class Graph_MST:
    def __init__(self, n: int = 0):
        self.num_vertex = n
        self.AdjList: list[deque[dict[int, int]]] = [deque() for _ in range(n)]
        self.predecessor: list[int] = [-1 for _ in range(n)]
        self.distance: list[int] = [math.inf for _ in range(n)]
        # initialize visited[] as {0,0,0,...,0}
        self.visited: list[bool] = [False for _ in range(n)]

    def __InitializeSingleSource(self, Start: int):  # 以Start作為起點
        self.distance[Start] = 0  # 起點vertex的distance設為0, ExtractMin就會從起點開始

    def __PrintDataArray(self, array: list[int]) -> None:
        for i in range(self.num_vertex):
            print("\t{0}".format(i), end="")
        print()

        for i in range(self.num_vertex):
            print("\t{0}".format(array[i]), end="")
        print()

    def AddEdge(self, source: int, destination: int, weight: int) -> None:
        self.AdjList[source].append({destination: weight})

    def Prim_MinQueue(self, Start: int) -> None:
        self.__InitializeSingleSource(Start)

        minQueue = BinaryHeap(self.num_vertex)
        # use minQueue to handle distance[]
        minQueue.BuildMinHeap(self.distance)
        minQueue.display()

        while not minQueue.IsHeapEmpty():
            u = minQueue.ExtractMin()
            minQueue.display()
            self.visited[u] = True

            for itr in iter(self.AdjList[u]):
                itr_item_to = list(itr.keys())[0]
                itr_item_weight = list(itr.values())[0]
                print("u: {0}, to: {1}, weight: {2}".format(
                    u, itr_item_to, itr_item_weight))
                if self.visited[itr_item_to] == False and\
                        itr_item_weight < self.distance[itr_item_to]:

                    '''
                    for edge(X,Y)
                    u: X , (*itr).first: Y, (*itr).second: weight(X,Y)
                    (*itr).second < distance[(*itr).first]: weight(X,Y) < distance[Y]
                    '''

                    self.distance[itr_item_to] = itr_item_weight
                    self.predecessor[itr_item_to] = u
                    minQueue.DecreaseKey(
                        itr_item_to, self.distance[itr_item_to])

        #######   print result   #######
        print("print predecessor[]")
        self.__PrintDataArray(self.predecessor)
        print("print distance[]")
        self.__PrintDataArray(self.distance)

        print("\tv1-\tv2: weight\n")
        i = (Start + 1) % self.num_vertex  # 若從4開始, i依序為5,6,0,1,2,3

        while i != Start:
            print(
                "\t{0}-\t{1} : \t{2}".format(self.predecessor[i], i, self.distance[i]))
            i += 1
            i %= self.num_vertex  # 到了6之後, 6+1 = 7, error:bad_access


def main():
    g6 = Graph_MST(7)

    g6.AddEdge(0, 1, 5)
    g6.AddEdge(0, 5, 3)
    g6.AddEdge(1, 0, 5)
    g6.AddEdge(1, 2, 10)
    g6.AddEdge(1, 4, 1)
    g6.AddEdge(1, 6, 4)
    g6.AddEdge(2, 1, 10)
    g6.AddEdge(2, 3, 5)
    g6.AddEdge(2, 6, 8)
    g6.AddEdge(3, 2, 5)
    g6.AddEdge(3, 4, 7)
    g6.AddEdge(3, 6, 9)
    g6.AddEdge(4, 1, 1)
    g6.AddEdge(4, 3, 7)
    g6.AddEdge(4, 5, 6)
    g6.AddEdge(4, 6, 2)
    g6.AddEdge(5, 0, 3)
    g6.AddEdge(5, 4, 6)
    g6.AddEdge(6, 1, 4)
    g6.AddEdge(6, 2, 8)
    g6.AddEdge(6, 3, 9)
    g6.AddEdge(6, 4, 2)

    print("MST found by Prim_MinQueue:\n")

    g6.Prim_MinQueue(2)


if __name__ == "__main__":
    main()
