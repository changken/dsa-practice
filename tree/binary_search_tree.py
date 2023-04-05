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

    def search(self, key):
        current = self.root

        # 1.沒找到
        # 2.找到
        while current is not None and current.info != key:
            if key < current.info:
                current = current.left #往左走
            else:
                current = current.right #往右走 
        
        return current

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
    
    def delete(self, key):
        delete_node = self.search(key)

        # 先確認BST中是否有具有KEY的node
        if delete_node is None:
            print("data not found!")
            return

        real_delete_node = None # 真正要被刪除並釋放記憶體的node
        delete_node_child = None # 要被刪除的node的"child"

        if delete_node.left is None or delete_node.right is None:
            real_delete_node = delete_node
        else:
            # 將real_delete_node設成delete_node的Successor
            real_delete_node = self.InorderSuccessor(delete_node)

        # 經過這組if-else, y調整成至多只有一個child
        # 全部調整成case1或case2來處理

        # 將 delete_node_child 設成 real_delete_node 的child, 可能是有效記憶體,
        # 也有可能是None
        if real_delete_node.left is not None:
            delete_node_child = real_delete_node.left
        else:
            delete_node_child = real_delete_node.right

        # 在 real_delete_node 被刪除之前, 這個步驟把 delete_node_child 接回BST
        if real_delete_node is not None:
            delete_node_child.parent = real_delete_node.parent # 此即為圖二(c)中, 把基紐接回龜仙人的步驟

        # 接著再把要被釋放記憶體的node之"parent"指向新的child
        if real_delete_node.parent is None:
            # 若刪除的是原先的root, 就把delete_node_child當成新的root 
            self.root = delete_node_child
        elif real_delete_node == real_delete_node.parent.left:
            # 若 real_delete_node 原本是其parent之left child
            # 便把 delete_node_child 皆在 real_delete_node 的parent的left child, 取代 real_delete_node
            real_delete_node.parent.left = delete_node_child
        else:
            # 若 real_delete_node 原本是其parent之right child
            # 便把 delete_node_child 皆在real_delete_node的parent的right child, 取代real_delete_node
            real_delete_node.parent.right = delete_node_child
        
        #針對case3
        if real_delete_node != delete_node:          # 若real_delete_node是delete_node的替身, 最後要再將real_delete_node的資料
            delete_node.info = real_delete_node.info # 放回delete_node的記憶體位置, 並將real_delete_node的記憶體位置釋放
                                                     # 圖二(d), y即是達爾, delete_node即是西魯

        del real_delete_node # 將real_delete_node的記憶體位置釋放
        real_delete_node = None

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

    print("5在不在? ", bst.search(5) is not None)
    print()
    print("11在不在? ", bst.search(11)  is not None)
    print()

    bst.delete(5)

    print("5在不在? ", bst.search(5) is not None)
    print()


if __name__ == "__main__":
    main()
