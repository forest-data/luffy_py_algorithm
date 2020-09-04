# AVL树 ： AVL树是一棵自平衡的二叉搜索树。 任何一个节点，两个子树的高度差不能超过1
# AVL树具有以下性质：
# 根的左右子树的高度之差的绝对值不能超过1
# 根的左右子树都是平衡二叉树

# balance factor 平衡因子  == 左子树高度 - 右子树高度



# AVL树 插入   破坏 > 旋转操作修正
from 数据结构.二叉树搜索树 import BiTreeNode, BST


class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0    # 用于存储平衡因子


class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    # 4个旋转
    # 左旋   K的右孩子的右子树插入
    def rotate_left(self, p, c):
        # 将s2接到p上
        s2 = c.lchild
        p.rchild = s2
        # s2连回去就需要判断一下
        if s2:
            s2.parent = p
        #
        c.lchild = p
        p.parent = c

        # 更新balance factor
        p.bf = 0
        c.bf = 0
        return c

    # 向右旋转
    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2

        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    # 右旋左旋： K的右孩子的左子树插入
    def rotate_right_left(self, p, c):
        g = c.lchild

        # 右旋
        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        #左旋
        s2 = g.lchild
        p.rchild = s2

        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # 更新bf   为什么是 右-左
        if g.bf > 0:    # 等于1 插入到s3上， 高度为h
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:    # 插入到s2上，高度为h，否则为h-1
            p.bf = 0
            c.bf = 1
        else:    # s1, s2, s3, s4 是空 ， 插入的是g
            p.bf = 0
            c.bf = 0
        return g

    def rotate_left_right(self, p, c):
        # 左旋
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c

        g.lchild = c
        c.parent = g

        # 右旋
        s3 = g.rchild
        p.lchild = s3

        if s3:
            s3.parent = p

        g.rchild = p
        p.parent = g

        # 更新bf
        if g.bf < 0:   # 插到s2上
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:   # 插入到s3
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0

        return g   # 返回根节点

    # 左来的 -1   右来的 +1   传递为0则保持不变



    # 插入
    def insert_no_rec(self, val):
        # 1. 和BST一样, 插入
        p = self.root
        if not p:  # 如果p为空
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild    # node存储的就是插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
                    # return
            else:    # val == p.data 等于  在AVL中，不要有相同的元素
                return



        # 2. 更新balance factor
        while node.parent:    # node.parent 不空
            if node.parent.lchild == node:    # 传递是从左子树来的，左子树更沉了
                # 更新node.parent 的 bf -= 1
                # 3种情况   -1  0   1
                if node.parent.bf < 0 :  #原来node.parent.bf == -1, 更新后边成 -2
                    # 做旋转
                    # 看node 那边沉
                    g = node.parent.parent    # 为了连接旋转之后的子树
                    x = node.parent    # 旋转前的子树的根
                    if node.bf > 0:   # 右边沉   左旋右旋
                        n = self.rotate_left_right(node.parent, node)
                    else: # 左边沉
                        n = self.rotate_right(node.parent, node)

                elif node.parent.bf > 0:   # 原来node.parent.bf = 1, 更新之后变成0
                    node.parent.bf = 0
                    break

                else:    # 原来的node.parent.bf = 0, 更新之后变成-1
                    node.parent.bf = -1
                    node = node.parent    # 继续往上更新
                    continue


            else:  # 传递是从右子树来的, 右子树更沉了
                # 更新node.parent.bf += 1
                if node.parent.bf > 0:    # 原来node.parent.bf == 1, 更新后变成2
                    # 做旋转
                    # 看node哪边沉
                    # 右边沉
                    g = node.parent.parent    # 为了连接旋转之后的子树
                    x = node.parent  # 旋转前的子树的根
                    if node.bf < 0:    # 左边沉  node.bf = 1
                        n = self.rotate_right_left(node.parent, node)
                    else:   # node.bf = -1
                        n = self.rotate_left(node.parent, node)

                    # 记得连起来

                elif node.parent.bf < 0:   # 原来 node.parent.bf = -1 , 更新之后变成0
                    node.parent.bf = 0
                    break   # 因为是0所以不用传递了

                else:  # 原来的node.parent.bf = 0, 更新之后变成1
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # 链接旋转后的子树
            n.parent = g
            if g:    # 如果g不是空
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break

            else:    # 如果g是空
                self.root = n
                break



# tree = AVLTree([7,3,5,4,2,8,6,9,1])

tree = AVLTree([9,8,7,6,5,4,3,2,1])
# tree.pre_order(tree.root)
print("开始测试")
tree.in_order(tree.root)

