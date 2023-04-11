from prim_algorithm_heap import BinaryHeap
from collections import deque
import math


class ToWeight:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight


class Graph_SP:
    def __init__(self, n: int = 0):
        self.num_vertex = n
        self.AdjList: list[deque[ToWeight]] = [deque() for _ in range(n)]

    def AddEdge(self, from_: int, to: int, weight: int):
        self.AdjList[from_].append(ToWeight(to, weight))

    def PrintDataArray(self, array: list[int]):
        for i in range(self.num_vertex):
            print(f"\t{i}", end="")
        print()

        for i in range(self.num_vertex):
            print(f"\t{array[i]}", end="")
        print()

    def PrintIntArray(self, array: list[int]):
        self.PrintDataArray(array)

    def InitializeSingleSource(self, Start: int):  # 以Start作為起點
        self.distance = [math.inf for _ in range(self.num_vertex)]
        self.predecessor = [-1 for _ in range(self.num_vertex)]
        self.distance[Start] = 0

    def Relax(self, from_: int, to: int, weight: int):  # edge方向：from X to Y
        if self.distance[to] > self.distance[from_] + weight:
            self.distance[to] = self.distance[from_] + weight
            self.predecessor[to] = from_

    def Dijkstra(self, Start: int = 0):  # 需要Min-Priority Queue
        self.InitializeSingleSource(Start)

        minQueue = BinaryHeap(self.num_vertex)  # object of min queue
        minQueue.BuildMinHeap(self.distance)
        minQueue.display()

        # initialize visited[] as {0,0,0,...,0}
        self.visited: list[bool] = [False for _ in range(self.num_vertex)]

        while not minQueue.IsHeapEmpty():
            u = minQueue.ExtractMin()
            minQueue.display()

            for itr in iter(self.AdjList[u]):
                print(itr.to, itr.weight)
                self.Relax(u, itr.to, itr.weight)
                minQueue.DecreaseKey(itr.to, self.distance[itr.to])

        print("\nPrint Predecessor[]:\n")
        self.PrintDataArray(self.predecessor)
        print("\nPrint Distance[]:\n")
        self.PrintDataArray(self.distance)


def main():
    g9 = Graph_SP(6)
    g9.AddEdge(0, 1, 8)
    g9.AddEdge(0, 5, 1)
    g9.AddEdge(1, 0, 3)
    g9.AddEdge(1, 2, 1)
    g9.AddEdge(2, 0, 5)
    g9.AddEdge(2, 3, 2)
    g9.AddEdge(2, 4, 2)
    g9.AddEdge(3, 1, 4)
    g9.AddEdge(3, 2, 6)
    g9.AddEdge(3, 4, 7)
    g9.AddEdge(3, 5, 3)
    g9.AddEdge(5, 3, 2)
    g9.AddEdge(5, 4, 8)

    g9.Dijkstra(0)


if __name__ == "__main__":
    main()
