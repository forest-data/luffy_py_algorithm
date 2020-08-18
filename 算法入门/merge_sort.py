
#归并排序
def merge_sort(li):
    n = len(li)

    # 递归结束条件
    if n<=1:
        return li

    # 中间位置
    mid = n // 2

    # 递归拆分左侧
    left_li = merge_sort(li[:mid])

    # 递归拆分右侧
    right_li = merge_sort(li[mid:])

    # 需要2个游标， 分别指向左列表和右列表第一个元素
    left_point, right_point = 0, 0

    # 定义最终返回的结果集
    result = []

    # 循环合并数据
    while left_point < len(left_li) and right_point < len(right_li):
        # 谁小放前面
        if left_li[left_point] <= right_li[right_point]:
            # 放进结果集
            result.append(left_li[left_point])
            left_point += 1
        else:
            result.append(right_li[right_point])
            right_point += 1

    # 退出循环是，形成左右两个序列
    result += left_li[left_point:]
    result += right_li[right_point:]

    return result


if __name__ == '__main__':
    li = [53, 26, 93, 17, 77, 31, 44, 55, 21]
    print(li)
    print(merge_sort(li))