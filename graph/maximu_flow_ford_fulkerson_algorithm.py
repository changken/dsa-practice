from collections import deque


class Graph_FlowNetWorks:
    def __init__(self, n=0):
        # constructor
        self.num_vertex = n
        self.AdjMatrix = [[0 for i in range(n)] for j in range(n)]
        self.visited = None
        self.predecessor = None
        self.graphResidual = None  # 預設為鄰接矩陣

    def initialize(self):
        self.visited = [0 for i in range(self.num_vertex)]  # 0 表示還沒有被找到
        self.predecessor = [-1 for i in range(self.num_vertex)]  # -1 表示沒有前驅節點

    def AddEdge(self, from_, to, weight):
        self.AdjMatrix[from_][to] = weight

    def BFSfindExistingPath(self, source: int, destination: int) -> None:
        self.initialize()
        queue = deque()

        # BFS 從 source 開始, 也可以規定source一律訂成vertex(0)
        queue.append(source)
        self.visited[source] = 1  # 找到source 設為1

        while len(queue):
            exploring = queue.popleft()  # 將排在queue前面的點取出
            for j in range(self.num_vertex):  # 檢查所有的點
                # 如果j與exploring有Edge且j沒被拜訪過
                if self.graphResidual[exploring][j] != 0 and self.visited[j] == 0:
                    queue.append(j)  # 將j加入queue
                    self.visited[j] = 1  # j設為已拜訪
                    self.predecessor[j] = exploring  # j的前驅節點為exploring

        # 也可以用 if (predecessor[t] != -1) 判斷
        # 若destination有被visited, 表示有path從source到destination
        return self.visited[destination] == 1

    def MinCapacity(self, destination: int) -> None:
        min = 100  # 確保min會更新, 假設graph上的capacity都小於100

        # 用predecessor[idx] 和 idx 表示一條edge
        # 找到在從source到destination的path上, capacity最小的值, 存入min
        idx = destination
        while self.predecessor[idx] != -1:  # 如果idx有前驅節點
            # idx與前驅節點有residual capacity且小於min
            if self.graphResidual[self.predecessor[idx]][idx] != 0 and self.graphResidual[self.predecessor[idx]][idx] < min:
                # 更新min為最小的capacity
                min = self.graphResidual[self.predecessor[idx]][idx]

            # idx變成前驅節點
            idx = self.predecessor[idx]

        return min

    def FordFulkerson(self, source: int, destination: int) -> None:
        # residual networks的初始狀態等於AdjMatrix, 見圖五(a)
        self.graphResidual = self.AdjMatrix.copy()
        maxFlow = 0

        # BFS finds augmenting path,
        while self.BFSfindExistingPath(source, destination):
            minCapacity = self.MinCapacity(
                destination)  # 取得最小的residual capacity
            maxFlow += minCapacity  # maxFlow加上最小的residual capacity

            Y = destination  # Y初始為destination
            while Y != source:  # Y不是source
                # 更新 residual graph
                X = self.predecessor[Y]  # X為Y的前驅節點
                # X到Y的capacity減去minCapacity
                self.graphResidual[X][Y] -= minCapacity
                # Y到X的capacity加上minCapacity
                self.graphResidual[Y][X] += minCapacity

                Y = self.predecessor[Y]  # Y變成前驅節點

        print(f"Possible Maximum FLow: {maxFlow}\n")  # 回傳最大流量


def main():
    g11 = Graph_FlowNetWorks(6)

    g11.AddEdge(0, 1, 9)
    g11.AddEdge(0, 3, 9)
    g11.AddEdge(1, 2, 3)
    g11.AddEdge(1, 3, 8)
    g11.AddEdge(2, 4, 2)
    g11.AddEdge(2, 5, 9)
    g11.AddEdge(3, 2, 7)
    g11.AddEdge(3, 4, 7)
    g11.AddEdge(4, 2, 4)
    g11.AddEdge(4, 5, 8)

    g11.FordFulkerson(0, 5)   # 指定source為vertex(0), termination為vertex(5)


if __name__ == "__main__":
    main()
