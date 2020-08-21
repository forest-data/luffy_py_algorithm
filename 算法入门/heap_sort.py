# _*_coding:utf-8_*_

# 堆排序


# 堆的向下调整
# 时间复杂度 O(logn)
def sift(li, low, high):
    """
    :param li: 列表
    :param low: 堆的根节点
    :param high: 堆的最后一个元素位置
    :return:
    """

    i = low   # i 最开始指向根节点
    j = 2 * i + 1    # j开始是左孩子

    tmp = li[low]   # 将堆顶存起来

    while j<=high:   # 只要j位置有效

        if j + 1 <= high and li[j+1] > li[j]: # 如果右孩子有，且比较大
            j = j + 1    # j指向右孩子

        if li[j] > tmp:
            li[i] = li[j]
            i = j   # 往下看一层
            j = 2 * i + 1
        else:    # tmp 更大， 把tmp放到i的位置上
            li[i] = tmp    # 把tmp放到某一级领导位置上
            break
    else:
        li[i] = tmp   # 把tmp放到叶子节点上


# 构建堆 + 排序
# 时间复杂度 O(nlogn)
def heap_sort(li):
    # 构建建堆
    n = len(li)
    for i in range(n-2//2, -1, -1):    #
        #i 表示建堆的时候调整的部分的根的下标
        sift(li,i,n-1)

    # 排序
    for i in range(n-1, -1, -1):
        # i 指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)    # i-1是新的high


# 实际表现  快排 > 堆排

li = [i for i in range(100)]
import random
random.shuffle(li)
print(li)
heap_sort(li)
print(li)


