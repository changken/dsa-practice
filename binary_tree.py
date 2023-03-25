class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.info = data
        self.parent = None


class BinaryTree:
    def __init__(self, char_strings):
        self.char_arr = char_strings.split(" ")

        self.root = TreeNode(self.char_arr[0])

        self.LevelorderConstruct(self.char_arr)

    def LevelorderConstruct(char_arr):
        pass

    def InsertLevelorder(data):
        pass

    def leftmost(current):
        while current.left is not None:
            current = current.left
        return current

    def InorderSuccessor(current):
        # 右子樹不為空，則右子樹的最左邊的節點為後繼者
        if current.right is not None:
            return self.leftmost(current.right)

        # 右子樹為空，則往上找，直到找到某個節點是其父節點的右子樹
        # 這個節點的父節點就是後繼者
        successor = current.parent
        while successor is not None and current is successor.right:
            current = successor
            successor = successor.parent

    def Inorder_by_parent(self):
        current = self.leftmost(self.root)

        while current is not None:
            print(current.info, end=" ")
            current = self.InorderSuccessor(current)


def main():
    pass


if __name__ == "__main__":
    main()
