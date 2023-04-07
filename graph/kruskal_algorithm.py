class Edge:
    def __init__(self, source: int, destination: int, weight: int):
        self.s = source
        self.d = destination
        self.w = weight


class GraphMST:
    def __init__(self, n: int = 0):
        self.num_vertex = n
        self.AdjMatrix = [[0 for j in range(n)] for i in range(n)]

    def AddEdge(self, source: int, destination: int, weight: int) -> None:
        self.AdjMatrix[source][destination] = weight

    def KruskalMST(self) -> None:
        # 在mst裡的edge
        edgesetMST: list[Edge] = [None for _ in range(self.num_vertex-1)]
        edgeset_count = 0
        # 管理頂點的subset
        subset: list[int] = [-1 for _ in range(self.num_vertex)]
        # 將edge依照weight作升序
        increaseWeight: list[Edge] = []
        self.GetSortedEdge(increaseWeight)  # 得到排好序的edge的vec

        for i in range(len(increaseWeight)):
            if FindSetCollapsing(subset, increaseWeight[i].s) != FindSetCollapsing(subset, increaseWeight[i].d):
                edgesetMST[edgeset_count] = increaseWeight[i]
                edgeset_count += 1
                UnionSet(subset, increaseWeight[i].s, increaseWeight[i].d)

        # 以下僅僅是印出vertex與vertex之predecessor
        print("\tv1-\tv2: weight")
        for i in range(self.num_vertex-1):
            print(
                "\t{0}-\t{1}: {2}".format(edgesetMST[i].s, edgesetMST[i].d, edgesetMST[i].w))

    def GetSortedEdge(self, edge_array: list[Edge]) -> None:
        for i in range(self.num_vertex):
            for j in range(i+1, self.num_vertex):
                if self.AdjMatrix[i][j] != 0:
                    edge_array.append(Edge(i, j, self.AdjMatrix[i][j]))

        # 用sorted 排序, 自己定義一個comparison
        edge_array.sort(key=lambda e: e.w)


def FindSetCollapsing(subset: list[int], i: int) -> int:
    # 找根節點
    root = i
    while subset[root] >= 0:
        root = subset[root]

    # 如果不是根節點，則將節點的父節點設為根節點
    while i != root:
        parent = subset[i]
        subset[i] = root
        i = parent

    return root


def UnionSet(subset: list[int], x: int, y: int) -> None:
    x_root = FindSetCollapsing(subset, x)
    y_root = FindSetCollapsing(subset, y)

    # 用rank比較, 負越多表示set越多element, 所以是值比較小的element比較多
    # xroot, yroot的subset[]一定都是負值
    if subset[x_root] <= subset[y_root]:
        subset[x_root] += subset[y_root]
        subset[y_root] = x_root
    else:  # if (subset[xroot] > subset[yroot]), 表示y比較多element
        subset[y_root] += subset[x_root]
        subset[x_root] = y_root


def WeightComp(e1: Edge, e2: Edge) -> bool:
    return e1.w < e2.w


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

    print("MST found by Kruskal:\n")
    g6.KruskalMST()


if __name__ == "__main__":
    main()
