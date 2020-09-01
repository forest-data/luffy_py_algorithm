# 二叉树
# 二叉树的链式存储：将二叉树的节点定义为一个对象，节点之间通过类似链表的链接方式来链接

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None    # 左孩子
        self.rchild = None    # 右孩子

a = BiTreeNode('A')
b = BiTreeNode('B')
c = BiTreeNode('C')
d = BiTreeNode('D')
e = BiTreeNode('E')
f = BiTreeNode('F')
g = BiTreeNode('G')

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e

print(root.lchild.rchild.data)


# 二叉树遍历 >  前序遍历   中序遍历   后序遍历   层次遍历

# 前序遍历
def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)



# 中序遍历
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=',')
        in_order(root.rchild)

# 后序遍历
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=',')

# 层次遍历
from collections import deque

def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:    # 只要队不空
        node = queue.popleft()    # 出队一个元素
        print(node.data, end=',')   # 访问出队元素
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


pre_order(root)
print('\n')
in_order(root)
print('\n')
post_order(root)
print('\n')
level_order(root)

print('\n' + '-' * 50 + '\n')

# 知道先序, 后序, 构建二叉树
# 通过前序遍历和中序遍历构建二叉树的原理，
# 主要是找前序遍历根节点在中序遍历中的位置，然后将二叉树而成左子树和右子树，然后依次进行这样的操作,思路还是比较简单的

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:    # 只要队不空
        node = queue.popleft()    # 出队一个元素
        print(node.data, end=',')   # 访问出队元素
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return queue

def construct_tree(pre_order, mid_order):
    # 忽略参数合法性判断
    if len(pre_order) == 0:
        return None
    # 前序遍历的第一个结点一定是根结点
    root_data = pre_order[0]
    i = mid_order.index(root_data)
    # 递归构造左子树和右子树
    left = construct_tree(pre_order[1: 1 + i], mid_order[:i])
    right = construct_tree(pre_order[1 + i:], mid_order[i + 1:])
    return Node(root_data, left, right)

pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
root = construct_tree(pre_order, mid_order)
level_order(root)