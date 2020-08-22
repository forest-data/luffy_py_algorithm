import random

'''
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

# 快速排序 > 划分交换排序
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] < tmp:
            left += 1
        li[right] = li[left]

    li[left] = tmp
    return left

def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)



li = list(range(10))
random.shuffle(li)
print(li)
partition(li, 0, len(li)-1)
quick_sort(li, 0, len(li)-1)
print(li)

# 归并排序



# 堆排序

# 堆的向下调整
def sift(li, low, high):

    i = low
    j = 2 * i + 1
    tmp = li[i]

    while j<=high:
        # 指针切换到右节点
        if j+1 <= high and li[j+1] > li[j]:
            j = j+1

        # 换位置
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2*i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

# 堆排序
def heap_sort(li):

    n = len(li)
    # 子节点 找 父节点   下标-1//2
    for i in range(n//2-1, -1, -1):
        sift(li, i, n-1)


    # 排序
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)


print('堆排序')
li = list(range(10))
random.shuffle(li)
print(li)

heap_sort(li)
print(li)

'''

# 快速排序 > 划分交换排序
# 划分
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] > tmp:
            right -= 1
        li[left] = li[right]
        print(li)
        while left<right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
        print(li)
        print('-' * 10)
    li[left] = tmp
    return left

def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)


# print('快速排序')
# li = list(range(10))
# random.shuffle(li)
li = [5, 8, 6, 2, 1, 5, 0]
print(li)
quick_sort(li, 0, len(li)-1)
print(li)













