import random
import time
# 查找算法

# 写一个装饰器，用于测试查找所使用的时间
def cal_time(func):
    def get_use_time(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print('%s running time: %s secs.' % (func.__name__, t2 - t1))
        return result

    return get_use_time


# 顺序查找
@cal_time
def linner_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None

# li = list(range(10))
# random.shuffle(li)
# print(li)
# print(linner_search(li, 3))


# 二分查找
@cal_time
def binary_search(li, val):
    left = 0
    right = len(li)-1
    while left <= right:
        mid = (left + right) // 2
        if val == li[mid]:
            return mid
        elif val > li[mid]:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return None
# 必须是顺序排序
# li = list(range(10))
# print(li)
# print(binary_search(li, 3))

# 测试性能
# li = list(range(10000000))
# print(binary_search(li, 565656))
# print(linner_search(li, 565656))


# Low B 三人组

# 冒泡排序 > 针对的是list, 核心 趟， 无序区间, O(n)

def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j] >= li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

# li = list(range(10))
# random.shuffle(li)
# print(li)
# print(bubble_sort(li))


# 选择排序 > 趟，无序区间, 位置
def select_sort(li):

    for i in range(len(li)-1):    # 趟数
        min_loc = i
        for j in range(i, len(li)-1):
            if li[min_loc] > li[j+1]:
                min_loc = j+1
        li[i], li[min_loc] = li[min_loc], li[i]

    return li

# li = list(range(10))
# random.shuffle(li)
# print(li)
# print(select_sort(li))

# 插入排序 > 抽取的趟数， while位移

def insert_sort(li):
    for i in range(len(li)-1):    # 待抽牌的位置
        tmp = li[i]
        j = i-1  # 已排好牌的位置
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1

        li[j+1] = tmp
    return li

# li = list(range(10))
# random.shuffle(li)
# print(li)
# print(insert_sort(li))


# 快速排序
# 先将第一个数，排到中间位置上
def partition(li, left, right):

    tmp = li[left]

    while left < right:

        while li[right] > tmp and left < right:
            right -= 1

        li[left] = li[right]

        while li[left] <= tmp and left < right:
            left += 1

        li[right] = li[left]

    li[left] = tmp

    return left

def quick_sort(li, left, right):

    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)

    return li

# li = list(range(10))
# random.shuffle(li)
# print(li)
# print(quick_sort(li, 0, len(li)-1))


# 堆排序  >  值交换

# 堆的向下调整

def sift(li, low, high):

    i = low
    j = 2 * i + 1
    tmp = li[i]

    while j<=high:

        if li[j] < li[j+1] and j+1 <= high:   # 如果有右孩子,且比较大
            j += 1

        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2*i + 1
        else:
            li[i] = tmp
            break

    else:
        li[i] = tmp


def heap_sort(li):
    # 构建堆，从农村开始
    # 从第一个非叶子节点开始
    n = len(li)-1
    for i in range((n-1)//2, -1, -1):
        sift(li, i, n)

    # 挨个出数
    for i in range(n-1, -1, -1):
        # i指向最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)

    return li

# li = list(range(10))
# random.shuffle(li)
# print(li)
# print(quick_sort(li, 0, len(li)-1))


# 归并排序

# 先实现合并上的排序
def merge(li, low, mid, high):

    i = low
    j = mid + 1
    ltmp = []

    while i <= mid and j<=high:
        if li[i] > li[j]:
            ltmp.append(li[j])
            j += 1
        else:
            ltmp.append(li[i])
            i += 1

    while i <= mid:
        ltmp.append(li[i])
        i += 1

    while j <= high:
        ltmp.append(li[j])
        j+=1

    li[low:high + 1] = ltmp

def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)  # 递归左边
        merge_sort(li, mid + 1, high)  # 递归右边
        merge(li, low, mid, high)
        print(li[low:high + 1])

li = list(range(10))
import random
random.shuffle(li)
print(li)
merge_sort(li, 0, len(li) - 1)
print(li)


