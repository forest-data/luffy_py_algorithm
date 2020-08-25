# 快速排序

def partition(li, left, right):
    tmp = li[left]

    while left < right:

        while li[right] > tmp and left < right:
            right -= 1
        li[left] = li[right]

        while li[left] <= tmp and left < right:
            left += 1
        li[right] = li[left]

    else:
        li[left] = tmp

    return left

def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)

    return li

# li = [5,7,4,6,3,1,2,9,8]
# print(li)
# print(quick_sort(li, 0, len(li)-1))

# 归并排序
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

    while j<= high:
        ltmp.append(li[j])
        j += 1

    li[low:high + 1] = ltmp

def merge_sort(li, low, high):
    if low < high:
        mid = (low + high)//2
        merge_sort(li, low, mid-1)
        merge_sort(li, mid+1, high)
        merge(li,low,mid,high)

    return li

# li = list(range(10))
# import random
# random.shuffle(li)
# print(li)
# print(merge_sort(li, 0, len(li)-1))


# 堆排序

def sift(li, low, high):

    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:

        if j+1 <= high and li[j] < li[j+1]:
            j = j+1

        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

def heap_sort(li):

    n = len(li)

    # 构建堆
    for i in range(n-2//2, -1, -1):
        sift(li, i, n-1)

    # 挨个出数，排序
    for i in range(n-1, -1, -1):
        # i指向最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)


li = [i for i in range(100)]
import random
random.shuffle(li)
print(li)
heap_sort(li)
print(li)




