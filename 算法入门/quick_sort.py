#
# 快速排序
def partition(li,left,right):

    tmp = li[left]

    while left < right:
        while left < right and li[right] >= tmp:    # 找比左边tmp小的数，从右边找
            right -= 1    # 往左走一步
        li[left] = li[right]    # 把右边的值写到左边空位上

        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]    #把左边的值写到右边空位上

    li[left] = tmp    # 把tmp归位
    return left


def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid-1)
        quick_sort(data, mid+1, right)


# li = [5,7,4,6,3,1,2,9,8]
# print(li)
# partition(li, 0, len(li)-1)
# quick_sort(li, 0, len(li)-1)

'''
# 快排
# first 第一索引位置， last 最后位置索引
# 时间复杂度  最坏O(n^2)  最优O(nlogn)
def quick_sort(li, first, last):
    # 递归终止条件
    if first >= last:
        return

    # 设置第一个元素为中间值
    mid_value = li[first]

    # low指向first
    low = first

    # high指向last
    high = last

    # 只要low < high 就一直走
    while low < high:
        # high 大于中间值， 则进入循环
        while low < high and li[high] >= mid_value:
            # high往左走
            high -= 1

        # 出循环后，说明high < mid_value, low指向该值
        li[low] = li[high]

        # high走完了，让low走
        # low小于中间值，则进入循环
        while low < high and li[low] < mid_value:
            low += 1
        # 出循环后，说明low > mid_value, high 指向该值
        li[high] = li[low]

        # 退出整个循环后， low和high相等
        li[low] = mid_value

        # 递归
        # 先对左侧快排
        quick_sort(li, first, low-1)
        # 对右侧快排
        quick_sort(li, low+1, last)
'''


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)
