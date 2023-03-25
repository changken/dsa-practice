from collections import deque


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.info = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            current = self.root

            while True:
                if data < current.info:
                    if current.left is None:
                        current.left = TreeNode(data)
                        current.left.parent = current
                        break
                    else:
                        current = current.left

                elif data > current.info:
                    if current.right is None:
                        current.right = TreeNode(data)
                        current.right.parent = current
                        break
                    else:
                        current = current.right

    def preOrder(self, root):
        if root is None:
            return
        else:
            print(root.info, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def inOrder(self, root):
        if root is None:
            return
        else:
            self.inOrder(root.left)
            print(root.info, end=" ")
            self.inOrder(root.right)

    def poseOrder(self, root):
        if root is None:
            return
        else:
            self.poseOrder(root.left)
            self.poseOrder(root.right)
            print(root.info, end=" ")

    def levelOrder(self):
        q = deque()
        q.append(self.root)

        while len(q):
            current = q.popleft()

            print(current.info, end=" ")

            if current.left is not None:
                q.append(current.left)

            if current.right is not None:
                q.append(current.right)

    # in order next node
    def InorderSuccessor(self, current):
        # 1. 右子樹不為空，則右子樹的最左邊的節點為後繼節點
        if current.right is not None:
            return self.leftmost(current.right)

        # 2. 右子樹為空，則往上找，直到找到某個節點是其父節點的左子樹，則該父節點為後繼節點
        successor = current.parent
        while successor is not None and current == successor.right:
            current = successor
            successor = successor.parent

        return successor

    # in order previos node
    def InorderPredecessor(self, current):
        # 1. 左子樹不為空，則左子樹的最右邊的節點為前驅節點
        if current.left is not None:
            return self.rightmost(current.left)

        # 2. 左子樹為空，則往上找，直到找到某個節點是其父節點的右子樹，則該父節點為前驅節點
        predecessor = current.parent
        while predecessor is not None and current == predecessor.left:
            current = predecessor
            predecessor = predecessor.parent

        return predecessor

    def leftmost(self, current):
        while current.left is not None:
            current = current.left

        return current

    def rightmost(self, current):
        while current.right is not None:
            current = current.right

        return current

    def Inorder_by_parent(self, root):
        current = self.leftmost(root)
        while current is not None:
            print(current.info, end=" ")
            current = self.InorderSuccessor(current)  # 找下一個節點

    def Inorder_Reverse(self, root):
        current = self.rightmost(root)

        while current is not None:
            print(current.info, end=" ")
            current = self.InorderPredecessor(current)  # 找上一個節點


def main():
    bst = BinarySearchTree()
    arr = [3, 4, 5, 7, 1, 2, 6, 9, 10, 8]
    for e in arr:
        bst.insert(e)
    bst.preOrder(bst.root)
    print()
    bst.inOrder(bst.root)
    print()
    bst.Inorder_by_parent(bst.root)
    print()
    bst.Inorder_Reverse(bst.root)
    print()
    bst.poseOrder(bst.root)
    print()
    bst.levelOrder()
    print()


if __name__ == "__main__":
    main()
