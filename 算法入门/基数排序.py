# 基数排序: 说白了就是 多条件查找
# 基数排序的效率跟数的范围有关，空间上需要消耗一个桶

# 时间复杂度 O(kn)    k=log(10,n)  n
# 快速排序  nlog(2,n)

'''
li = [random.randint(0,1000000) for _ in range(1000)]
                          k                      n
'''

def radix_sort(li):
    max_num = max(li)   # 最大值 99-2  888-3   10000-5  位数是几，那就做几次循环
    it = 0   # 类似 个位，十位，百位
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]   # 10个桶   # 下标代表相应的数字位
        # 分桶
        for var in li:
            digit = (var // 10 ** it) % 10    # 得出个位数，十位数，百位数
            buckets[digit].append(var)
        # 分桶完成

        # 把数重新写回li
        li.clear()
        for buc in buckets:
            li.extend(buc)

        it += 1

import random
li = list(range(10000))
random.shuffle(li)
radix_sort(li)
print(li)



# 应用
"""
字符串比较
abcd
ab00

小数 > 不太好弄

"""
