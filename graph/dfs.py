from collections import deque


class Graph:
    def __init__(self, N=0) -> None:
        self.num_vertex = N
        self.adjList = [deque() for _ in range(N)]  # initialize Adj List
        # 配置記憶體位置
        self.color = [0] * N  # 0 = 白色, 1 = 灰色, 2 = 黑色
        self.discover = [0] * N
        self.finish = [0] * N
        self.predecessor = [-1] * N
        self.time = 0  # 初始化, 如圖三(b)

    def addEdgeList(self, from_e: int, to_e: int) -> None:
        self.adjList[from_e].append(to_e)

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


def main():
    # 定義一個具有八個vertex的Graph
    g2 = Graph(8)
    # 建立如圖三之Graph
    g2.addEdgeList(0, 1)
    g2.addEdgeList(0, 2)
    g2.addEdgeList(1, 3)
    g2.addEdgeList(2, 1)
    g2.addEdgeList(2, 5)
    g2.addEdgeList(3, 4)
    g2.addEdgeList(3, 5)
    # AdjList[4] is empty
    g2.addEdgeList(5, 1)
    g2.addEdgeList(6, 4)
    g2.addEdgeList(6, 7)
    g2.addEdgeList(7, 6)

    g2.dfs(0)    # 以vertex(0), 也就是vertex(A作為DFS()的起點


if __name__ == "__main__":
    main()
