import math


class Graph_SP_AllPairs:
    def __init__(self, n=0):
        self.num_vertex = n
        # Constructor, initialize AdjMatrix with 0 or MaxDistance
        self.AdjMatrix = [[0 if i == j else math.inf for i in range(n)] for j in range(n)]
        self.Distance = [[math.inf for i in range(n)] for j in range(n)]
        self.Predecessor = [[-1 for i in range(n)] for j in range(n)]

    def AddEdge(self, from_, to, weight):
        self.AdjMatrix[from_][to] = weight

    def PrintData(self, array):
        for i in range(self.num_vertex):
            for j in range(self.num_vertex):
                print(f"\t{array[i][j]}", end="")
            print()

    def InitializeData(self):
        for i in range(self.num_vertex):
            for j in range(self.num_vertex):
                self.Distance[i][j] = self.AdjMatrix[i][j]
                if self.Distance[i][j] != 0 and self.Distance[i][j] != math.inf:
                    self.Predecessor[i][j] = i

    def FloydWarshall(self):
        self.InitializeData()

        print("initial Distance[]:\n")
        self.PrintData(self.Distance)
        print("\ninitial Predecessor[]:\n")
        self.PrintData(self.Predecessor)

        for k in range(self.num_vertex):
            print(f"\nincluding vertex=({k}):\n")
            for i in range(self.num_vertex):
                for j in range(self.num_vertex):
                    self.Relax(i, j, k)
            # print data after including new vertex and updating the shortest paths
            print("Distance[]:\n")
            self.PrintData(self.Distance)
            print("\nPredecessor[]:\n")
            self.PrintData(self.Predecessor)

    def Relax(self, i, j, k):
        if (self.Distance[i][j] > self.Distance[i][k] + self.Distance[k][j])\
                and self.Distance[i][k] != math.inf:
            self.Distance[i][j] = self.Distance[i][k] + self.Distance[k][j]
            self.Predecessor[i][j] = self.Predecessor[k][j]


def main():
    g10 = Graph_SP_AllPairs(4)
    g10.AddEdge(0, 1, 2)
    g10.AddEdge(0, 2, 6)
    g10.AddEdge(0, 3, 8)
    g10.AddEdge(1, 2, -2)
    g10.AddEdge(1, 3, 3)
    g10.AddEdge(2, 0, 4)
    g10.AddEdge(2, 3, 1)

    g10.FloydWarshall()


if __name__ == "__main__":
    main()
