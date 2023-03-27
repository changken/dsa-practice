class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.info = data
        self.color = False  # False -> Red, True -> Black


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.neel = TreeNode(None)

    def left_rotation(self, x):
        y = x.right  # 把y指向x的rightchild, 最後y會變成x的parent
        x.right = y.left  # 圖二(c)左, 把y的leftchild托在x的rightchild

        if y.left != self.neel:  # 圖二(c)右, 若node(j)為NIL則忽略
            y.left.parent = x  # 將原先y的leftchild的parent改成x

        y.parent = x.parent  # 圖二(d)左, 更新y的parent

        if x.parent == self.neel:
            self.root = y       # 圖二(d)右, 若原先x是root, 旋轉後y變成新的root
        elif x == x.parent.left:  # 若原先x是其parent的leftchild
            x.parent.left = y   # 更新後y也是其parent的leftchild
        else:                   # 若原先x是其parent的rightchild
            x.parent.right = y  # 更新後y也是其parent的rightchild

        y.left = x   # 圖二(e)左, 最後才修改y與x
        x.parent = y  # 圖二(e)右

    def right_rotation(self, y):
        x = y.left  # 把x設成y的leftchild
        y.left = x.right  # 把x的rightchild放到y的leftchild

        if x.right != self.neel:  # 若x的rightchild不為NIL, 將其parent指向y
            x.right.parent = y

        x.parent = y.parent  # 將x的parent指向原先y的parent

        # 以下一組if-else將修改原先y的parent之child
        if y.parent == self.neel:  # 若y原先是root, x將成為新的root
            self.root = x
        elif y == y.parent.left:  # 若原先y是其parent之leftchild,
            y.parent.left = x  # x就成為其新的parent之leftchild
        else: # 若原先y是其parent之rightchild, 
            y.parent.right = x  # x就成為其新的parent之rightchild

        x.right = y  # 將y設為x之rightchild
        y.parent = x # 將x設為y之parent
    