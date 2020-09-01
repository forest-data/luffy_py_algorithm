from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None    # 左孩子
        self.rchild = None    # 右孩子
        self.parent = None    # 双链表

# 二叉搜索树的操作：查询、插入、删除
# 二叉搜索树：左<根<右
# Binary search tree

# 插入
class BST:

    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)


    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)

        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        else:  # val == node.data  找到了就停止
            pass


        return node


    # 非递归实现插入
    def insert_no_rec(self, val):
        p = self.root
        if not p: # 如果p为空
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:    # 左孩子不存在
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    # 前序遍历
    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    # 中序遍历
    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    # 后序遍历
    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')


tree = BST([4,6,7,9,2,1,3,5,8])
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)
print("")
tree.post_order(tree.root)

import random

li = list(range(100))
random.shuffle(li)
