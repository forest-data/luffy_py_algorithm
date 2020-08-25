# 桶排序：从计数排序演变过来

# 桶排序时间复杂度
'''
平均时间复杂度： O(n+k)
最坏 O(n^2k)
空间复杂度 O(nk)   因为桶排序占用了一个桶的空间
k = logm*logn
n 是列表长度
m 是桶的个数
'''
# n 表示桶的个数   max_num 表示数的最大
def bucket_sort(li, n=100, max_num=10000):
    # 创建桶
    buckets = [[] for _ in range(n)]

    # 遍历列表中的每个数
    for var in li:
        # (max_num//n) 表每个桶放多少个数
        # i表示 var放到哪个桶里面
        i= min(var // (max_num//n), n-1)
        buckets[i].append(var)

        # 保持桶里面的顺序
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break

    sorted_li = []

    for buc in buckets:
        sorted_li.extend(buc)

    return sorted_li

import random

li = [random.randint(0, 10000) for i in range(10000)]
print(li)

print(bucket_sort(li))
