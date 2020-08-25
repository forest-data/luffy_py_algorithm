
# 希尔排序 ： 是一种分组插入排序算法.
# 时间复杂和gap序列有关
def insert_sort_gap(li, gap):

    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
            li[j+gap] = tmp

def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d//=2

li = list(range(1000))
import random
random.shuffle(li)
print(li)
shell_sort(li)
print(li)
