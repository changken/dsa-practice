import strongly_connected_component


class GraphTopological(strongly_connected_component.Graph):
    def topologicalSort(self, start: int = 0):
        self.VariableInitializeDFS()
        self.dfs(start)  # 進行一次DFS用來取得 finish[]

        # 矩陣 finishLargetoSmall[] 用來儲存 finish[] 由大至小的vertex順序
        finishLargetoSmall = [i for i in range(self.num_vertex)]

        # QuickSort()會更新 finishLargetoSmall[] 成 finish[] 由大至小的vertex順序
        self.quickSort(self.finish, 0, self.num_vertex-1, finishLargetoSmall)

        print("Topological Sort:\n")
        for i in range(self.num_vertex):
            print("   {0}".format(finishLargetoSmall[i]), end=" ")
        print()


def main():
    g5 = GraphTopological(15)            # 建立如圖二(a)的DAG
    g5.addEdgeList(0, 2)
    g5.addEdgeList(1, 2)
    g5.addEdgeList(2, 6)
    g5.addEdgeList(2, 7)
    g5.addEdgeList(3, 4)
    g5.addEdgeList(4, 5)
    g5.addEdgeList(5, 6)
    g5.addEdgeList(5, 14)
    g5.addEdgeList(6, 8)
    g5.addEdgeList(6, 9)
    g5.addEdgeList(6, 11)
    g5.addEdgeList(6, 12)
    g5.addEdgeList(7, 8)
    g5.addEdgeList(9, 10)
    g5.addEdgeList(12, 13)

    g5.topologicalSort()
    g5.topologicalSort(4)


if __name__ == "__main__":
    main()
