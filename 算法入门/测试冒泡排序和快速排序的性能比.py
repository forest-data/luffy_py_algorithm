

# 冒泡排序 : 趟，无序区间
import copy
import random

from 算法入门.cal_time import cal_time

@cal_time
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

    return li



# 快速排序

def partition(li, left, right):
    tmp = li[left]

    while left < right:
        while li[right] >= tmp and left < right:
            right -= 1

        li[left] = li[right]

        while li[left] < tmp and left < right:
            left += 1

        li[right] = li[left]

    li[left] = tmp

    return left

def _quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)

    return li

@cal_time
def quick_sort(li):
    li = _quick_sort(li, 0, len(li)-1)
    return li


# cpu读取速度 10^7/s
li = list(range(10000))
random.shuffle(li)
print(li)
# 递归最大次数为999，如何更改呢?
import sys
sys.setrecursionlimit(100000)

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)

print(quick_sort(li1))
print(bubble_sort(li2))



