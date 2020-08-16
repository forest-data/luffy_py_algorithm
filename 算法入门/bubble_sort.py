import random

# 冒泡排序：  一趟一趟将大的值往上放。  关键点：趟、无序区范围
# 时间复杂度： O(n^2)

def bubble_sort(li):
    for i in range(len(li)-1):   # 第i趟  从第0趟开始
        # 优化
        exchange = False
        for j in range(len(li)-1-i):    # 无序区范围
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True

        if not exchange:    # 如果没有交换
            return


li = [random.randint(0, 100) for i in range(10)]
print(li)

bubble_sort(li)
print(li)
