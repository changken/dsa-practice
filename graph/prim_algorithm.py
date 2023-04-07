import math


class GraphMST:
    def __init__(self, n=0):
        self.num_vertex = n
        self.AdjMatrix = [[0 for j in range(n)] for i in range(n)]

    def AddEdge(self, source: int, destination: int, weight: int) -> None:
        self.AdjMatrix[source][destination] = weight

    # 可以指定起點Start, 若沒有指定, 則從vertex(0)作為MST的root
    def PrimMST(self, Start: int = 0) -> None:
        key = [math.inf for _ in range(self.num_vertex)]
        predecessor = [-1 for _ in range(self.num_vertex)]
        # false表示vertex還沒有被visited
        visited = [False for _ in range(self.num_vertex)]

        key[Start] = 0

        for i in range(self.num_vertex):
            # 找目前最小的key, 並且還沒有被visited
            u = self.MinKeyExtract(key, visited, self.num_vertex)
            # 將vertex u加入MST
            visited[u] = True

            for j in range(self.num_vertex):
                # 如果vertex j 還沒有被拜訪 且
                # vertex u 與 j 之間有邊 且
                # vertex j 的current key值大於 vertex u 與 j之間邊的weight
                if visited[j] == False and \
                        self.AdjMatrix[u][j] != 0 and \
                        self.AdjMatrix[u][j] < key[j]:
                    predecessor[j] = u  # 將vertex u設為vertex j的predecessor
                    key[j] = self.AdjMatrix[u][j]  # 更新vertex j的 current key值

        self.printMST(Start, predecessor)

    def MinKeyExtract(self, key: list[int], visited: list[int], size: int) -> int:
        min = math.inf
        min_idx = 0
        for i in range(size):
            if visited[i] == False and key[i] < min:
                min = key[i]
                min_idx = i

        return min_idx

    # print MST, 與MST演算法主體無關
    def printMST(self, Start: int = 0, predecessor: list[int] = None) -> None:
        print("\tv1-\tv2: weight")
        i = (Start + 1) % self.num_vertex  # 若從4開始, i依序為5,6,0,1,2,3

        while i != Start:
            print(
                "\t{0}-\t{1} : \t{2}".format(predecessor[i], i, self.AdjMatrix[predecessor[i]][i]))
            # 到了6之後, 6+1 = 7, error:bad_access, 透過mod把7喬回0
            i += 1
            i = (i) % self.num_vertex


def main():
    g6 = GraphMST(7)
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

    print("MST found by Prim:\n")
    g6.PrimMST(2)


if __name__ == "__main__":
    main()
