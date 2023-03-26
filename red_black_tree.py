class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.info = data
        self.color = False  # False -> Red, True -> Black


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.nil = TreeNode(None)
