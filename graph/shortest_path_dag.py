from collections import deque
import math
from collections import deque


class ToWeight:
    def __init__(self, to: int, weight: int):
        self.to = to
        self.weight = weight


class Graph_SP:  # SP serves as Shortest Path
    def __init__(self, n: int = 0):
        self.num_vertex = n
        self.AdjList: list[deque[ToWeight]] = [deque() for _ in range(n)]
        self.predecessor = None
        self.distance = None
        # dfs
        self.color = [0 for _ in range(self.num_vertex)]
        self.discover = [0 for _ in range(self.num_vertex)]
        self.finish = [0 for _ in range(self.num_vertex)]
        self.time = 0
        self.count = self.num_vertex - 1  # count 為 topologicalsort[] 的 index

        # topological sort
        self.topologicalsort: list[int] = [0 for _ in range(self.num_vertex)]

    def AddEdge(self, from_: int, to: int, weight: int) -> None:
        self.AdjList[from_].append(ToWeight(to, weight))

    def PrintDataArray(self, array: list[int]) -> None:
        for i in range(self.num_vertex):
            print("\t{0}".format(i), end="")
        print()

        for i in range(self.num_vertex):
            print("\t{0}".format(array[i]), end="")
        print()

    def PrintIntArray(self, array: list[int]) -> None:
        for i in range(self.num_vertex):
            print("\t{0}".format(i), end="")
        print()

        for i in range(self.num_vertex):
            print("\t{0}".format(array[i]), end="")
        print()

    def InitializeSingleSource(self, Start: int) -> None:  # 以Start作為起點
        self.distance = [math.inf for _ in range(self.num_vertex)]
        self.predecessor = [-1 for _ in range(self.num_vertex)]
        self.distance[Start] = 0

    def Relax(self, from_: int, to: int, weight: int) -> None:  # 對edge(X,Y)進行Relax
        if self.distance[to] > self.distance[from_] + weight:
            self.distance[to] = self.distance[from_] + weight
            self.predecessor[to] = from_

    def DAG_SP(self, Start: int = 0) -> None:  # 需要 DFS, 加一個額外的Linked list
        # distance[],predecessor[]的initialization
        self.InitializeSingleSource(Start)

        self.GetTopologicalSort(Start)  # 得到topological sort

        for i in range(self.num_vertex):
            v = self.topologicalsort[i]
            for itr in self.AdjList[v]:
                self.Relax(v, itr.to, itr.weight)

        print("\nPrint Predecessor: \n")
        self.PrintIntArray(self.predecessor)
        print("\nPrint Distance: \n")
        self.PrintIntArray(self.distance)

    def GetTopologicalSort(self, Start: int) -> None:
        self.predecessor = [-1 for _ in range(self.num_vertex)]
        i = Start

        for j in range(self.num_vertex):
            if self.color[i] == 0:
                self.DFSVisit_TS(i)
            i = j

        print("\nPrint Discover time: \n")
        self.PrintIntArray(self.discover)
        print("\nPrint Finish time: \n")
        self.PrintIntArray(self.finish)

    def DFSVisit_TS(self, vertex: int) -> None:
        self.color[vertex] = 1  # set gray
        self.time += 1
        self.discover[vertex] = self.time
        for itr in self.AdjList[vertex]:
            if self.color[itr.to] == 0:
                self.predecessor[itr.to] = vertex
                self.DFSVisit_TS(itr.to)

        self.color[vertex] = 2  # set black
        self.time += 1
        self.finish[vertex] = self.time
        self.topologicalsort[self.count] = vertex  # 產生Topological Sort
        self.count -= 1


def main():
    g8 = Graph_SP(7)
    g8.AddEdge(0, 1, 3)
    g8.AddEdge(0, 2, -2)
    g8.AddEdge(1, 3, -4)
    g8.AddEdge(1, 4, 4)
    g8.AddEdge(2, 4, 5)
    g8.AddEdge(2, 5, 6)
    g8.AddEdge(3, 5, 8)
    g8.AddEdge(3, 6, 2)
    g8.AddEdge(4, 3, -3)
    g8.AddEdge(4, 6, -2)
    g8.AddEdge(5, 6, 2)

    # g8.DAG_SP(0)  # 以vertex(0)作為起點
    g8.DAG_SP(2)  # 以vertex(2)作為起點


if __name__ == "__main__":
    main()
