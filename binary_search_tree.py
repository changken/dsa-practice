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


def main():
    bst = BinarySearchTree()
    arr = [3, 4, 5, 7, 1, 2, 6, 9, 10, 8]
    for e in arr:
        bst.insert(e)
    bst.preOrder(bst.root)
    print()
    bst.inOrder(bst.root)
    print()
    bst.poseOrder(bst.root)
    print()
    bst.levelOrder()
    print()


if __name__ == "__main__":
    main()
