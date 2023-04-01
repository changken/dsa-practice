from collections import deque


class Graph:
    # default constructor
    # constructor with input: number of vertex
    def __init__(self, N=0):
        self.num_vertex = N
        self.adjList = [deque() for _ in range(N)]  # initialize Adjacency List
        self.color = [0] * N  # 0:白色=>預設, 1:灰色, 2:黑色
        self.distance = [N+1] * N  # 0:起點, 無限大:從起點走不到的vertex
        # num_vertex個vertex, 最長距離 distance = num_vertex -1條edge
        self.predecessor = [-1] * N  # -1:沒有predecessor(預設), 表示為起點vertex

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


def main():
    g1 = Graph(9)

    # 建立出圖二(a)的Adjacency List
    g1.addEdgeList(0, 1)
    g1.addEdgeList(0, 2)
    g1.addEdgeList(0, 3)
    g1.addEdgeList(1, 0)
    g1.addEdgeList(1, 4)
    g1.addEdgeList(2, 0)
    g1.addEdgeList(2, 4)
    g1.addEdgeList(2, 5)
    g1.addEdgeList(2, 6)
    g1.addEdgeList(2, 7)
    g1.addEdgeList(3, 0)
    g1.addEdgeList(3, 7)
    g1.addEdgeList(4, 1)
    g1.addEdgeList(4, 2)
    g1.addEdgeList(4, 5)
    g1.addEdgeList(5, 2)
    g1.addEdgeList(5, 4)
    g1.addEdgeList(5, 8)
    g1.addEdgeList(6, 2)
    g1.addEdgeList(6, 7)
    g1.addEdgeList(6, 8)
    g1.addEdgeList(7, 2)
    g1.addEdgeList(7, 3)
    g1.addEdgeList(7, 6)
    g1.addEdgeList(8, 5)
    g1.addEdgeList(8, 6)

    g1.bfs(0)

    print(g1.color)
    print(g1.distance)
    print(g1.predecessor)


if __name__ == "__main__":
    main()
