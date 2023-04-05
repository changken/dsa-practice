from collections import deque


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.info = data
        self.parent = None


class BinaryTree:
    def __init__(self, char_strings):
        char_arr = char_strings.split(" ")

        self.root = TreeNode(char_arr[0])

        self.LevelOrderConstruct(char_arr[1:])

    def LevelOrderConstruct(self, char_arr):
        q = deque()
        current = self.root

        for i in range(0, len(char_arr), 2):
            if char_arr[i] >= 'A' and char_arr[i] <= 'Z':
                current.left = TreeNode(char_arr[i])
                current.left.parent = current
                q.append(current.left)

            if char_arr[i+1] >= 'A' and char_arr[i+1] <= 'Z':
                current.right = TreeNode(char_arr[i+1])
                current.right.parent = current
                q.append(current.right)

            current = q.popleft()

    def InsertLevelOrder(self, data):
        q = deque()
        current = self.root

        while current:
            if current.left is not None:
                q.append(current.left)
            else:
                current.left = TreeNode(data)
                current.left.parent = current
                break

            if current.right is not None:
                q.append(current.right)
            else:
                current.right = TreeNode(data)
                current.right.parent = current
                break

            current = q.popleft()

    def leftmost(self, current):
        while current.left is not None:
            current = current.left
        return current

    def InOrderSuccessor(self, current):
        # 右子樹不為空，則右子樹的最左邊的節點為後繼者
        if current.right is not None:
            return self.leftmost(current.right)

        # 右子樹為空，則往上找，直到找到某個節點是其父節點的右子樹
        # 這個節點的父節點就是後繼者
        successor = current.parent
        while successor is not None and current is successor.right:
            current = successor
            successor = successor.parent

        return successor

    def InOrder_by_parent(self):
        current = self.leftmost(self.root)

        while current is not None:
            print(current.info, end=" ")
            current = self.InOrderSuccessor(current)


def main():
    char_strings = "A B C D E F x x x G H x I"
    T = BinaryTree(char_strings)  # 以level-order規則建立Binary Tree
    T.InOrder_by_parent()  # 以inorder-traversal印出Binary Tree
    print()

    T.InsertLevelOrder('K')
    T.InsertLevelOrder('L')
    T.InsertLevelOrder('M')
    T.InsertLevelOrder('N')
    T.InOrder_by_parent()
    print()


if __name__ == "__main__":
    main()
