class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.height = 0

    def getHeight(self):
        return self.height


class AVLTree:
    def __init__(self):
        self.root = None

    def traverseRoot(self):
        self.traverse(self.root)

    def traverse(self, node):
        if node is None:
            return

        self.traverse(node.left)
        print(" -> {0}".format(node.key))
        self.traverse(node.right)

    def getNodeHeight(self, node):
        if node is None:
            return -1
        return node.getHeight()

    def getBalanceFactor(self, node):
        if node is None:
            return 0

        return self.getNodeHeight(node.left) - self.getNodeHeight(node.right)

    def rightRotation(self, node):
        print("Perform right rotation on node: {0}".format(node.key))

        # nodes relate to right rotation
        left_child = node.left
        temp_node = left_child.right

        # update node reference
        node.left = temp_node
        left_child.right = node

        # update node height, child must update height first
        self.updateNodeHeight(node)
        self.updateNodeHeight(left_child)

        return left_child

    def leftRotation(self, node):
        print("Perform left rotation on node:{0}".format(node.key))

        # nodes relate to right rotation
        right_child = node.right
        temp_node = right_child.left

        # update node reference
        node.right = temp_node
        right_child.left = node

        # update node height, child must update height first
        self.updateNodeHeight(node)
        self.updateNodeHeight(right_child)

        return right_child

    def findElement(self, key):
        if self.root is None:
            return None

        return self.find(key, self.root)

    def find(self, key, node):
        if node is None:
            return None

        if node.key < key:
            return self.find(key, node.right)
        elif node.key > key:
            return self.find(key, node.left)
        else:
            return node

    def insertElement(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self.root = self.insert(key, self.root)

    def insert(self, key, current_node):
        if current_node is None:
            return TreeNode(key)

        if current_node.key < key:
            current_node.right = self.insert(key, current_node.right)
        else:
            current_node.left = self.insert(key, current_node.left)

        # update node height and balance after inserting the node
        self.updateNodeHeight(current_node)
        current_node = self.updateTreeBalance(current_node)

        return current_node

    def updateNodeHeight(self, node):
        if node is None:
            return
        node.height = max(self.getNodeHeight(node.left),
                          self.getNodeHeight(node.right)) + 1

    def updateTreeBalance(self, node):
        bf = self.getBalanceFactor(node)

        if bf > 1:
            # 檢查左側還是右側的樹看哪邊比較重，右邊比較重，則為LR，左邊比較重則是LL
            if(self.getBalanceFactor(node.left) == 1):
                # LL Type
                return self.rightRotation(node)
            else:
                # LR Type
                node.left = self.leftRotation(node.left)
                return self.rightRotation(node)
        elif bf < -1:
            # 檢查左側還是右側的樹看哪邊比較重，右邊比較重，則為RR，左邊比較重則是RL
            if self.getBalanceFactor(node.right) == -1:
                # RR Type
                return self.leftRotation(node)
            else:
                # RL Type
                node.right = self.rightRotation(node.right)
                return self.leftRotation(node)

        return node

    def deleteElement(self, key):
        if self.root is None:
            return None

        root = self.delete(key, self.root)

        return root

    def delete(self, key, current_node):
        if current_node is None:
            return None

        if current_node.key < key:
            current_node.right = self.delete(key, current_node.right)
        elif current_node.key > key:
            current_node.left = self.delete(key, current_node.left)
        else:
            # case 1: target data is a leaf node
            if current_node.left is None and current_node.right is None:
                return None
            # case 2: target data only has right child
            elif current_node.right is not None:
                return current_node.right
            # case 3: target data only has left child
            elif current_node.left is not None:
                return current_node.left
            # case 4: target data has left and right child
            else:
                left_max_value_node = self.findMaxValueNode(current_node.left)

                # swap the data
                current_node.key, left_max_value_node.key = left_max_value_node.key, current_node.key

                # delete the data
                current_node.left = self.delete(
                    key, current_node.left)

        # update tree height
        self.updateNodeHeight(current_node)

        # update tree balance
        return self.updateTreeBalance(current_node)

    def findMaxValueNode(self, node):
        if node is None:
            return None
        if node.right is not None:
            return self.findMaxValueNode(node.right)
        return node


def main():
    avl = AVLTree()
    test_arr = range(1, 10)
    for i in test_arr:
        avl.insertElement(i)

    avl.traverseRoot()

    print(avl.findElement(5) is not None)
    avl.deleteElement(5)
    avl.traverseRoot()


if __name__ == "__main__":
    main()
