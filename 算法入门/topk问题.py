# 从list中取出前k个大的值

# 解决思路
# 排序后切片  O(nlogn + k)
# 排序LowB三人组  O(kn)   冒泡: m趟 O(kn)     特性： 一趟上去一个数
# 以上两种 取决于 logn 和 k的大小

# 堆排序：O(n logk)


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

        if j + 1 <= high and li[j+1] < li[j]: # 如果右孩子有，且比较大
            j = j + 1    # j指向右孩子

        if li[j] < tmp:
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


def topk(li, k):
    # 取出列表前k个
    heap= li[0:k]

    # 1. 建堆
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)

    # 2. 遍历
    for i in range(k, len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)

    # 3. 挨个出数
    for i in range(k-1, -1, -1):
        heap[0] , heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)

    return heap

import random
li = list(range(100))
random.shuffle(li)
print(li)
print(topk(li, 10))

