
# 插入排序  >  有序区1张牌  无序区n-1张牌
# 插入排序复杂度  O(n^2)

def insert_sort(li):
    # range 左闭右开
    for i in range(1, len(li)):   # i 表示每次抽牌的下标
        tmp = li[i]   # 抽牌的值
        j = i-1   #手里拍的下标
        while li[j]>tmp and j>=0:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp   # 为什么是li[j+1] ,是while循环结束后，j自减1


li = [3,2,4,1,5,6,8,9]
insert_sort(li)
print(li)

#