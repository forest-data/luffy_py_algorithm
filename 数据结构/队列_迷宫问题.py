from collections import deque

# 队列 -- 广度优先遍历
# 思想: 从一个节点开始， 寻找所有接下来能继续走的点，继续不断寻找，直到找到出口
# 使用队列存储当前正在考虑的节点

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x,y : (x-1, y),    # 上
    lambda x,y : (x+1, y),    # 下
    lambda x,y : (x, y-1),    # 左
    lambda x,y : (x, y+1)     # 右
]


def print_r(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] == -1:
        # realpath.append(curNode[0], curNode[1]) == realpath.append(curNode[0:2])
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]   # 下一个节点，curNode[2] 为位置 ， path存的是每个位置的值

    realpath.append(curNode[0:2])   # 到起点

    realpath.reverse()
    print(realpath)

def maze_path_queue(x1, y1, x2, y2):
    queue = deque()

    queue.append((x1, y1, -1))

    path = []   # 用于存放 出队的元素

    while len(queue) > 0 :  # 只要队不空，接着往下走。  如果 队空就没有路  则说明此路不通了

        curNode = queue.pop()   # 队首出栈

        path.append(curNode)

        if curNode[0] == x2 and curNode[1] == y2:
            # 终点
            print_r(path)

            return True

        for dir in dirs:

            nextNode = dir(curNode[0], curNode[1])   # 看这个节点是不是能走

            if maze[nextNode[0]][nextNode[1]] == 0:   # 如果可以走
                # len(path) - 1  如果此时找到3条路，那么这3个点的的源头 一定来自于 path 的最后一个元素的下标

                # 后续节点进队，记录哪个节点带它来的
                queue.append((nextNode[0], nextNode[1], len(path) - 1))    # 那么将该节点存下来， 第三个参数是 从哪里来的。

                # 接着 走过依然 标记为 2
                maze[nextNode[0]][nextNode[1]] == 2  # 标记为已经走过

                #
    else:
        print('没有路')
        return False

maze_path_queue(2,0,7,7)






