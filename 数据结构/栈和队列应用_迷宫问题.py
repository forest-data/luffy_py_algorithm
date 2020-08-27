# 栈 - 用栈来存储当前的路劲。 使用栈来做 思想：深度优先搜索：一条路走到黑   回溯法：回退到上一个点寻找是否有其他可走
# 缺点： 路径不一定是最短路径

# maze  迷宫   1 代表墙   0代表可走

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
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


def maze_path(x1, y1, x2, y2):  # (x1, y1) 起点位置   (x2, y2) 终点位置

    stack = []

    stack.append((x1, y1))   # 起点   最开始栈中有起点

    # 能找到一个位置，就压在栈中。 栈空 表示 死路

    # 只要栈不空
    while(len(stack) > 0):

        curNode = stack[-1]
        # 当前方向x,y   四个方向： 上 x-1 y  右 x, y+1   下 x+1, y  左 x, y-1
        # 当前点的下一个点

        # 如何判断到达终点呢？
        if curNode[0] == x2 and curNode[1] == y2:
            # 走到终点
            for p in stack:
                print(p)
            return True

        for dir in dirs:

            nextNode = dir(curNode[0], curNode[1])
            # 如果下一个节点能走, 就将节点添加到栈中。
            if maze[nextNode[0]][nextNode[1]] == 0:   # 判断能不能走，就是数组中的值等于0
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2    # 标记   2表示已经走过
                break    # 能找到一个就break
        else:   #一个都找不到
            maze[nextNode[0]][nextNode[1]] = 2  # 标记
            stack.pop()   # 回退
    else:

        print('没有路')
        return False


maze_path(2,0,7,7)






