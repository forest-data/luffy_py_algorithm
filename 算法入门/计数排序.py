# 计数排序：对列表进行排序， 已知列表中的数范围都在0-100之间，设计时间复杂度为O(n)的算法。
# 比较排序 最快 O(nlogn)

'''
 1 3 2 4 1 2 3 1 3 5
 列表索引   个数
 0          0
 1          3
 2          2
 3          3
 4          1
 5          1
 根据上方得出
 1 1 1 2 2 3 3 3 4 5
'''

# O(n)
import copy

from 算法入门.cal_time import cal_time

# 知道数的范围
@cal_time
def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count + 1)]

    # 得出每个值有多少个   因为这里循环n次， n是li的长度
    for val in li:
        count[val] += 1

    li.clear()   # 清空，用于存放排序的值

    # ind 是这个数值， val是有几个该数
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)     # 这里也是n次

@cal_time
def sys_sort(li):
    li.sort()

import random
li = [random.randint(0,100) for _ in range(100000)]
print(li)
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
count_sort(li1)
print(li1)

sys_sort(li2)
print(li2)



