class TreeNode:
    def __init__(self, key, strs):
        self.left = None
        self.right = None
        self.key = key  # node's key
        self.strs = strs  # node's string data
        self.color = False  # False -> Red, True -> Black


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.neel = TreeNode(None, None)

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
        else:  # 若原先y是其parent之rightchild,
            y.parent.right = x  # x就成為其新的parent之rightchild

        x.right = y  # 將y設為x之rightchild
        y.parent = x  # 將x設為y之parent

    def insert(self, key, strs):
        # 前半部與 InsertBST()之邏輯完全相同, 僅僅需要修改 NULL <-> NIL
        y = self.neel  # root的上一個
        x = self.root  # 初始為root
        insert_node = TreeNode(key, strs)

        while x != self.neel:  # 把root初始化成neel, 這裡就可以用neel來做判斷
            y = x
            if insert_node.key < x.key:
                x = x.left
            else:
                x = x.right

        insert_node.parent = y

        if y == self.neel:
            self.root = insert_node
        elif insert_node.key < y.key:
            y.left = insert_node
        else:
            y.right = insert_node

        # 以下是對RBT之node的設定, 將child pointer指向NIL, 顏色設為紅色
        insert_node.left = self.neel
        insert_node.right = self.neel
        insert_node.color = False  # 顏色可以在constructor中預設

        self.insert_fixup(insert_node)  # 對可能出現紅色與紅色node相連之情形做修正

    def insert_fixup(self, current):
        # case0: parent是黑色, 就不用進回圈
        while(current.parent.color == False):  # 若parent是紅色即進入迴圈
            # 上半部：parent是grandparent的left child
            if current.parent == current.parent.parent.left:
                uncle = current.parent.parent.right

                # case1: 若uncle是紅色
                if uncle.color == False:
                    current.parent.color = True
                    uncle.color = True
                    current.parent.parent.color = False  # grandparent改成紅色
                    current = current.parent.parent
                # case2 & 3: uncle是黑色
                else:
                    if current == current.parent.right:  # case2
                        current = current.parent
                        self.left_rotation(current)
                    # case3
                    current.parent.color = True  # 把parent塗黑
                    current.parent.parent.color = False  # grandparent塗紅
                    self.right_rotation(current.parent.parent)
            # 下半部：parent是grandparent的right child, 與上半部對稱
            else:
                uncle = current.parent.parent.left

                # case1: 若uncle是紅色
                if uncle.color == False:
                    current.parent.color = True
                    uncle.color = True
                    current.parent.parent.color = False  # grandparent改成紅色
                    current = current.parent.parent
                # case2 & 3: uncle是黑色
                else:
                    if current == current.parent.left:  # case2
                        current = current.parent
                        self.right_rotation(current)
                    # case3
                    current.parent.color = True  # 把parent塗黑
                    current.parent.parent.color = False  # grandparent塗紅
                    self.left_rotation(current.parent.parent)

        self.root.color = True  # 確保root是黑色
