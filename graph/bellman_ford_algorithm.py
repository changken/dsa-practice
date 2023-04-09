from collections import deque
import math


class ToWeight:
    def __init__(self, to: int, weight: int):
        self.to = to
        self.weight = weight
        self.predecessor = None
        self.distance = None


class Graph_SP:  # SP serves as Shortest Path
    def __init__(self, n=0):
        self.num_vertex = n
        self.AdjList: list[deque[ToWeight]] = [deque() for _ in range(n)]

    def AddEdge(self, source: int, destination: int, weight: int) -> None:
        self.AdjList[source].append(ToWeight(destination, weight))

    def PrintDataArray(self, array: list[int]):
        for i in range(self.num_vertex):
            print("\t{0}".format(i), end="")
        print()

        for i in range(self.num_vertex):
            print("\t{0}".format(array[i]), end="")
        print("\n")

    def InitializeSingleSource(self, Start: int) -> None:  # 以Start作為起點
        self.predecessor = [-1 for _ in range(self.num_vertex)]
        self.distance = [math.inf for _ in range(self.num_vertex)]

        self.distance[Start] = 0

    def Relax(self, source: int, destination: int, weight: int) -> None:  # 對edge(X,Y)進行Relax
        if self.distance[destination] > self.distance[source] + weight:
            self.distance[destination] = self.distance[source] + weight
            self.predecessor[destination] = source

    # 以Start作為起點
    # if there is negative cycle, return false
    def BellmanFord(self, Start: int = 0) -> bool:
        self.InitializeSingleSource(Start)

        for i in range(self.num_vertex - 1):  # |V-1|次的iteration
            # for each edge belonging to E(G)
            for j in range(self.num_vertex):  # 把AdjList最外層的vector走一遍
                for itr in self.AdjList[j]:  # 各個vector中, 所有edge走一遍
                    self.Relax(j, itr.to, itr.weight)

        # check if there is negative cycle
        for i in range(self.num_vertex):
            for itr in self.AdjList[i]:
                if self.distance[itr.to] > self.distance[i] + itr.weight: # i是from, itr是to
                    return False
        
        print("Predecessor[]: \n")
        self.PrintDataArray(self.predecessor)
        print("Distance[]: \n")
        self.PrintDataArray(self.distance)

        return True

def main():
    g7 = Graph_SP(6)
    g7.AddEdge(0, 1, 5)
    g7.AddEdge(1, 4, -4)
    g7.AddEdge(1, 2, 6)
    g7.AddEdge(2, 4, -3)
    g7.AddEdge(2, 5, -2)
    g7.AddEdge(3, 2, 4)
    g7.AddEdge(4, 3, 1)
    g7.AddEdge(4, 5, 6)
    g7.AddEdge(5, 0, 3)
    g7.AddEdge(5, 1, 7)

    if g7.BellmanFord(0):
        print("There is no negative cycle.\n")
    else:
        print("There is negative cycle.\n")


if __name__ == "__main__":
    main()
