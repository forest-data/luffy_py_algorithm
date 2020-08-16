
# 题目： n个盘子时， 从a  经过b  到c
# 流程
# n-1个盘子先到b > # n-1个盘子在到c

def hanoi(n, a, b, c):
    if n>0:    #
        hanoi(n-1, a, c, b)   # n-1个盘子先到b
        print('moving from %s to %s' % (a, c))
        hanoi(n-1, b, a, c)   # n-1个盘子在到c


hanoi(3, 'A', 'B', 'C')