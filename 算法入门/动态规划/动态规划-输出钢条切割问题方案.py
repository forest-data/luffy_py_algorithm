
# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# 输出最优切割方案
def cut_rod_extend(p, n):
    r = [0]   # 最大收益
    s = [0]   # 记录下刀最大收益的位置

    for i in range(1, n+1):   # 这个是循环p价格表
        res_r = 0    # 记录价格的最优值
        res_s = 0    # 价格最大值对应方案的左边不切割部分的长度
        for j in range(1, i+1):    # 这个是循环r价格表
            if p[j] + r[i-j] > res_r:
                res_r = p[j] + r[i-j]
                res_s = j

        r.append(res_r)
        s.append(res_s)

    return r[n], s

# 输出方案   10m  切割成几米是最优方案
def cut_rod_solution(p, n):
    r, s = cut_rod_extend(p, n)
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]

    return ans



r, s = cut_rod_extend(p, 10)
print(s)

# 输出切割方案
print(cut_rod_solution(p, 9))

# 应用场景   和最优值相关的问题， 求最优值的时候。
# 贪心算法是动态规划的一个特例。