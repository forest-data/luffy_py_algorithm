# 贪心算法： 贪婪算法，总是做出当前最好的选择。

# 1.找零问题
# 假设商店⽼老老板需要找零n元钱，钱币的⾯面额有:100元、50元、 20元、5元、1元，如何找零使得所需钱币的数量量最少?

t = [100, 50, 20, 5, 1, 2]   # 有多少种面币
# t.sort(reverse=True)

def change(t, n):
    """
    :param t: 有多少种面币
    :param n: 找零多少
    :return:
    """
    # n = 376
    # m = [1,2,0,0,0] # 张数

    m = [0 for _ in range(len(t))]

    for i, money in enumerate(t):
        m[i] = n//t[i]   # 整除
        n = n % money    # 剩余

    return m, n

# print(change(t, 376))



# 2.背包问题
# ⼀一个⼩小偷在某个商店发现有n个商品，第i个商品价值vi元，重wi千克。
# 他希望 拿⾛走的价值尽量量⾼高，但他的背包最多只能容纳W千克的东⻄西。他应该拿⾛走哪些 商品?

# 分数背包   >   最优

goods = [(60, 10), (120, 30), (100, 20)] # 每个商品元组表示  (价值，重量)
goods.sort(key=lambda x: x[0]/x[1], reverse=True)
print(goods)

def fractional_backpack(goods, w):    # w为背包的容量

    m = [0 for _ in range(len(goods))]   # m表示，每个商品拿多少走
    total_v = 0

    for i,(price, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1   # 全仓拿走
            total_v += price
            w -= weight    # 剩余背包的容量
        else:
            m[i] = w/weight
            total_v += m[i] * price
            w = 0
            break

    return total_v,m


print(fractional_backpack(goods, 50))


# 0-1背包   >   不一定


# 3. 拼接最大数字问题

# 分析思路
'''
a = "96"
b = "87"

a + b if a > b else b + a

a = "128"
b = "1286"

a + b = "1281286"
b + a = "1286128"

a + b if a+b > b+a else b+a

a = "728"
b = "7286"

a+b = "7287286"
b+a = "7286728"
'''
from functools import cmp_to_key

# 数字拼接 实现代码
li = [32,94,128,1286,6,71]

def xy_cmp(x, y):
    if x+y < y+x:
        return 1
    elif x+y > y+x:
        return -1
    else:    # 相等
        return 0


def number_join(li):

    li = list(map(str, li))

    # 对li进行排序
    li.sort(key= cmp_to_key(xy_cmp))
    print(li)

    return "".join(li)


print(number_join(li))


# 方式二  冒泡排序来做   趟， 无序区间
def bubble_sort(li):

    for i in range(len(li)-1):    # 趟
        for j in range(len(li) - i - 1):    #
            if li[j]+li[j+1] < li[j+1] + li[j]:   # 将最小的往后排
                li[j], li[j+1] = li[j+1], li[j]

    str = "".join(li)
    return str

li = list(map(str, li))
print(bubble_sort(li))


# 4.活动选择问题   >  贪最先结束时间
# 假设有n个活动，这些活动要占⽤用同⼀一⽚片场地，⽽而场地在某时刻只能供⼀一个活动使⽤用。
# 问:安排哪些活动能够使该场地举办的活动的个数最多?

# 一个元组表示一个活动 （开始时间，结束时间）
activities = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11),(8,12), (2,14), (12,16)]

# 保证活动是按照结束时间排好序的
activities.sort(key= lambda x: x[1])   # 按结束时间排序

def activity_selection(a):   # a就是活动
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] >= res[-1][1]:    # 如果当前活动的开始时间 >= 最后一个活动入选的结束事件
            # 不冲突
            res.append(a[i])

    return res

print(activity_selection(activities))

# 穷举法为什么是 2^n 次方 ？
# [1,2,3]   排序规则 000  001  010  011 100  101  110  111   n是列表元素个数