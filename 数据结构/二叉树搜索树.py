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
# 时间复杂度 O(logn)
# 最坏情况下：二叉搜索树可能非常偏斜


class BST:

    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    # 插入
    # 递归实现
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

    # 查询
    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node

    # 非递归实现查询
    def query_no_rec(self,val):
        p = self.root   # 从根节点开始
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None


    # 删除  3种情况
    def __remove_node_1(self, node):
        # 情况1: node是叶子节点
        if not node.parent:   # 如果是根节点      node.parent == None  只有根节点满足
            self.root = None

        if node == node.parent.lchild:  # node是它父亲的左孩子
            node.parent.lchild = None
        else:    # node是它父亲的右孩子
            node.parent.rchild = None

    #
    def __remove_node_21(self, node):
        # 情况21： node只有一个左孩子
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else: # 如果它是它父亲的右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # 情况22： node只有一个右孩子
        if not node.parent:    # 是否为根节点
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:    # 如果它是它父亲的左孩子，它只有一个右孩子
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else: # 如果它是它父亲的右孩子, 它只有一个右孩子
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        # 情况3：删除的节点 带有左右两孩子节点
        if self.root:    # 如果不是空树
            node = self.query_no_rec(val)
            if not node:   # 不存在
                return False
            if not node.lchild and not node.rchild:    # 叶子节点
                self.__remove_node_1(node)
            elif not node.rchild:     # 什么时候只有左孩子 和 右孩子？  2.1 如果它没有右孩子，那就只有一个左孩子
                self.__remove_node_21(node)
            elif not node.lchild:    # 2.2 只有一个右孩子
                self.__remove_node_22(node)
            else:   # 情况3: 两个孩子都有
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data

                # 删除min_node
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)

# 插入
tree = BST([4,6,7,9,2,1,3,5,8])
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)
print("")
tree.post_order(tree.root)

import random

li = list(range(100))
random.shuffle(li)

# 查询
print('\n' + '-' * 20)
li = list(range(0, 500, 2))
random.shuffle(li)
tree = BST(li)
print(tree.query_no_rec(4))

# 删除
tree = BST([1,4,2,5,3,8,6,9,7])
tree.in_order(tree.root)
print("")

tree.delete(4)
tree.in_order(tree.root)

