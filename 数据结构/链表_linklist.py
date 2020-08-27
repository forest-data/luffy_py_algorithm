# 链表定义
class Node:

    def __init__(self, item):
        self.item = item   # 值
        self.next = None


# a = Node(1)
# b = Node(2)
# c = Node(3)
#
# a.next = b
# b.next = c
#
# print(a.next.next.item)    # 3



# 如何创建列表： 1.头插法   2.尾插法
# 头插法   维护头部
def create_linklist_head(li):    # 通过列表循环插入
    head = Node(li[0])

    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node

    return head


# 尾插法   有头部 和 尾部
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head

    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node  # 尾节点

    return head


# 打印链表
def print_linklist(lk):
    while lk:
        print(lk.item, end = ',')
        lk = lk.next


# lk = create_linklist_head([1,2,3])
# print(lk.item)

lk = create_linklist_tail([1,2,3])
# print(lk)   # 头节点
print_linklist(lk)


# 链表插入删除O(1)
# 链表不是顺序存储, 链式存储结构

# 列表插入删除，时间复杂度O(n)， 【1，2，3，4】
#                                5，插入中间位置， 后方的都要挪动


'''
链表 与 顺序表 比较
1. 按元素查找   O(n)
2. 按下标查找   顺序O(1)   链表O(n)
3. 插入删除     顺序O(n)   链表O(1)

'''
# 双链表

