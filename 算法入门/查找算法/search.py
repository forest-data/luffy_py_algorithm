import random
# 查找： 目的都是从列表中找出一个值

# 顺序查找 > O(n)  顺序进行搜索元素
from 算法入门.cal_time import cal_time


@cal_time
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None

# 二分查找 > O(logn)  应用于已经排序的数据结构上
@cal_time
def binary_search(li, val):
    left = 0    # 坐下标
    right = len(li) - 1   #右下标
    while left <= right:    # 候选区有值
        mid = (left + right)//2 # 对2进行整除，向下取整
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None
# 测试
# li = [i for i in range(10)]
# random.shuffle(li)
# print(li)
#
# print(binary_search(li, 3))

# 性能比较
li = list(range(10000000))
linear_search(li, 3890)
binary_search(li, 3890)