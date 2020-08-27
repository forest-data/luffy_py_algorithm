# 树 是一种可以递归定义的数据结构

# 模拟系统的目录结构

class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type    # 'dir' or 'file'
        self.children = []
        self.parent = None
        # 链式存储

    def __repr__(self):
        return self.name

# n1 = Node('hello')
# n2 = Node('world')
# n1.children.append(n2)

class FileSystemTree:
    def __init__(self):
        self.root = Node('/')
        self.now = self.root

    def mkdir(self, name):
        # name 以 / 结尾
        if name[-1] != "/" : #
            name += "/"

        node = Node(name)   # 创建一个文件夹
        self.now.children.append(node)    # 与父文件关联起来
        node.parent = self.now


    def ls(self):
        return self.now.children     # 返回当前目录的所有子目录

    def cd(self, name):
        if name[-1] != '/':
            name += '/'

        if name == '../':
            self.now = self.now.parent
            return

        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise ValueError('invalid dir')

tree = FileSystemTree()
tree.mkdir('var/')
tree.mkdir('bin/')
tree.mkdir('usr/')

# print(tree.root.children)
tree.cd('bin/')
tree.mkdir('python/')

print(tree.ls())