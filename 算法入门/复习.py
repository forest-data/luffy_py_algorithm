import random

# 顺序查找
def linner_search(li, v):
    for ind, val in enumerate(li):
        if v==val:
            return ind
    else:
        return None

li = list(range(10))
# print(li)
# print(linner_search(li, 3))

# 二分查找
def binary_search(li, val):
    left = 0
    right = len(li)-1

    while left < right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return None

# print(binary_search(li, 5))


# 排序算法

# 冒泡排序: 趟 + 无序区间
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

li = [i for i in range(10)]
random.shuffle(li)
print(li)
# print(bubble_sort(li))

# 选择排序： 趟， 标记
def select_sort(li):
    for i in range(len(li)):
        min_loc = i
        for j in range(i, len(li)):
            if li[min_loc] > li[j]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc],li[i]

    return li

print(select_sort(li))

# 插入排序: 趟， while
def insert_sort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i-1
        while li[j] > tmp and j>0:
            li[j+1] = li[j]
            j -= 1
        li[j + 1] = tmp
    return li

print(insert_sort(li))