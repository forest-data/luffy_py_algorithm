
# 简单选择排序算法
def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new
# li = [3,2,4,1,5,6,8,7,9]
# print(select_sort_simple(li))


# 选择排序算法 > O(n^2)    记录最小下标
def select_sort(li):
    for i in range(len(li)-1):   # i是第几趟
        min_loc = i   #最小值位置
        for j in range(i+1, len(li)):  # j 无序区范围
            if li[min_loc] > li[j] :
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]

    return li
li = [3,2,4,1,5,6,8,7,9]
print(select_sort(li))