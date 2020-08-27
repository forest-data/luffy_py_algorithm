# python的字典和集合 都是采用这种方式来实现的

# 哈希表：一个通过哈希函数来计算数据存储位置的数据结构


class LinkList:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None


    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item

            else:
                raise StopIteration

        def __iter__(self):
            return self



    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)


    def append(self, obj):   # 队尾插入
        s = LinkList.Node(obj)     # 创建节点
        if not self.head:     # 如果为空
            self.head = s
            self.tail = s
        else:
            self.tail.next = s   # 尾部跟尾部接起来
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    # iter返回的是什么呢, 就是一个迭代对象, 它主要映射到了类里面的__iter__函数, 此函数返回的是一个实现了__next__的对象。
    # 迭代器类
    def __iter__(self):
        return self.LinkListIterator(self.head)

    # 事实上,当我们输出某个实例化对象时,其调用的就是该对象的 __repr__() 方法,输出的是该方法的返回值。
    def __repr__(self):
        return "<<"+", ".join(map(str,self))+">>"


# lk = LinkList([1,2,3,4,5])
# print(lk)   # <<1, 2, 3, 4, 5>>   返回的是 __repr__返回的值
# for element in lk:
#     print(element)


# 哈希表    类似于集合的结构
class HashTable:
    def __init__(self, size = 101):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]

    # 哈希函数
    def h(self, k):
        return k % self.size

    def insert(self, k):
        i = self.h(k)

        if self.find(k):
            print('Duplicated Insert .')
        else:
            self.T[i].append(k)

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)


ht = HashTable()
ht.insert(0)
ht.insert(1)
ht.insert(3)
ht.insert(102)

print(','.join(map(str, ht.T)))

print(ht.find(102))
