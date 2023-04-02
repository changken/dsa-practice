from collections import deque


class Graph:
    def __init__(self, N=0):
        self.num_vertex = N
        self.adjList = [deque() for _ in range(N)]  # initialize Adj List
        self.color = [0 for _ in range(N)]  # 0 白色, 1 灰色, 2 黑色
        self.predecessor = [-1 for _ in range(N)]
        self.distance = [N+1 for _ in range(N)]  # BFS
        self.discover = [0 for _ in range(N)]  # DFS
        self.finish = [0 for _ in range(N)]
        self.time = 0  # BFS

    def addEdgeList(self, from_e: int, to_e: int) -> None:
        self.adjList[from_e].append(to_e)

    def bfs(self, start: int) -> None:
        q = deque()
        i = start

        for j in range(self.num_vertex):  # j從0數到num_vertex-1, 因此j會走過graph中所有vertex
            if self.color[i] == 0:  # 第一次i會是起點vertex, 如圖二(c)
                self.color[i] = 1  # 1:灰色
                self.distance[i] = 0  # 每一個connected component的起點之距離設成0
                # 每一個connected component的起點沒有predecessor
                self.predecessor[i] = -1
                q.append(i)

                while len(q):
                    u = q.popleft()  # u 為新的搜尋起點

                    for itr in self.adjList[u]:
                        if self.color[itr] == 0:  # 若被「找到」的vertex是白色
                            self.color[itr] = 1  # 塗成灰色, 表示已經被「找到」
                            # 距離是predecessor之距離加一
                            self.distance[itr] = self.distance[u] + 1
                            # 更新被「找到」的vertex的predecessor
                            self.predecessor[itr] = u
                            q.append(itr)  # 把vertex推進queue

                    self.color[u] = 2  # 並且把u塗成黑色

            # 若一次回圈沒有把所有vertex走過, 表示graph有多個connected component
            # 就把i另成j, 繼續檢查graph中的其他vertex是否仍是白色, 若是, 重複while loop
            i = j

    def dfs(self, start: int) -> None:
        i = start
        for j in range(self.num_vertex):  # 檢查所有Graph中的vertex都要被搜尋到
            if self.color[i] == 0:  # 若vertex不是白色, 則進行以該vertex作為起點之搜尋
                self.dfsVisit(i)
            i = j  # j會把AdjList完整走過一遍, 確保所有vertex都被搜尋過

        # after for loop
        print("predecessor:")  # 印出 A(0) ~ H(7)的predecessor
        for i in range(self.num_vertex):
            print("    {0}".format(i), end=" ")
        print()
        for i in range(self.num_vertex):
            print("    {0}".format(self.predecessor[i]), end=" ")
        print()

        print("discover time:")  # 印出 A(0) ~ H(7)的discover time
        for i in range(self.num_vertex):
            print("    {0}".format(i), end=" ")
        print()
        for i in range(self.num_vertex):
            print("    {0}".format(self.discover[i]), end=" ")
        print()

        print("finish time:")  # 印出 A(0) ~ H(7)的finish time
        for i in range(self.num_vertex):
            print("    {0}".format(i), end=" ")
        print()
        for i in range(self.num_vertex):
            print("    {0}".format(self.finish[i]), end=" ")
        print()

    def dfsVisit(self, vertex: int) -> None:  # 一旦有vertex被發現而且是白色, 便進入DFSVisit()
        self.color[vertex] = 1  # 把vertex塗成灰色
        self.time += 1
        self.discover[vertex] = self.time  # 更新vertex的discover時間
        for itr in self.adjList[vertex]:
            if self.color[itr] == 0:  # 若搜尋到白色的vertex
                self.predecessor[itr] = vertex  # 更新其predecessor
                self.dfsVisit(itr)  # 立刻以其作為新的搜尋起點, 進入新的DFSVisit()

        self.color[vertex] = 2  # 當vertex已經搜尋過所有與之相連的vertex後, 將其塗黑
        self.time += 1
        self.finish[vertex] = self.time  # 並更新finish時間

    def setCollapsing(self, current: int) -> None:
        # 找每個component的root
        root = current
        while self.predecessor[root] >= 0:
            root = self.predecessor[root]
        
        # 將每個vertex的predecessor設成root
        while current != root:
                parent = self.predecessor[current]
                self.predecessor[current] = root
                current = parent

    def CCDFS(self, vertex: int) -> None:
        self.dfs(vertex)
        self.printPredecessor()
        for i in range(self.num_vertex):
            self.setCollapsing(i)
        self.printPredecessor()
        self.printComponent()

    def CCBFS(self, vertex: int) -> None:
        self.bfs(vertex)
        self.printPredecessor()
        for i in range(self.num_vertex):
            self.setCollapsing(i)
        self.printPredecessor()

        self.printComponent()

    def printPredecessor(self) -> None:  # 印出predecessor, 供驗証用, 非必要
        print("predecessor:")
        for i in range(self.num_vertex):
            print("    {0}".format(i), end=" ")
        print()
        for i in range(self.num_vertex):
            print("    {0}".format(self.predecessor[i]), end=" ")
        print()

    def printComponent(self) -> None:
        num_cc = 0
        for i in range(self.num_vertex):
            if self.predecessor[i] < 0:
                num_cc += 1
                print("Component#{0}: {1}".format(num_cc, i), end=" ")
                for j in range(self.num_vertex):
                    if self.predecessor[j] == i:
                        print(j, end=" ")
                print()


def main():
    g3 = Graph(9)
    g3.addEdgeList(0, 1)
    g3.addEdgeList(1, 0)
    g3.addEdgeList(1, 4)
    g3.addEdgeList(1, 5)
    # AdjList[2] empty
    g3.addEdgeList(3, 6)
    g3.addEdgeList(4, 1)
    g3.addEdgeList(4, 5)
    g3.addEdgeList(5, 1)
    g3.addEdgeList(5, 4)
    g3.addEdgeList(5, 7)
    g3.addEdgeList(6, 3)
    g3.addEdgeList(6, 8)
    g3.addEdgeList(7, 5)
    g3.addEdgeList(8, 6)

    g3.CCDFS(0)
    print()
    g3.CCBFS(0)
    print()


if __name__ == "__main__":
    main()
