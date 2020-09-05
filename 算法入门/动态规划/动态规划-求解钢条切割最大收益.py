
# 动态规划： 是一种算法思想，算法套路。 基因匹对，序列的相似程度。

# 钢条切割问题   >  动态规划所需的就是最优子结构， 递推式
# 百度整数分割问题
# 子问题的最优解，能够构造出大问题的最优解  >  最优子结构

# 递归实现
import time

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time : %s secs. " % (func.__name__, t2 - t1))
        return result

    return wrapper

# 给定的价格表， 长度是1的卖1块钱
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# 自顶向下实现
# 递归实现
def cut_rod_recurision_1(p, n):    # n 表钢条长度
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recurision_1(p, i) + cut_rod_recurision_1(p, n-i))   # res 是最大售价

        return res


# 单递归实现：左边不切割，右边切割    cut_rod_recurision_2返回的是n 米的最大收益
def cut_rod_recurision_2(p, n):    # n 表钢条长度
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n+1):
            res = max(res, p[i]+cut_rod_recurision_2(p, n-i))   # res 是最大收益
        return res

# 注意： 给递归函数加装饰器，就会递归装饰。 疯狂输出
# print(cut_rod_recurision_1(p, 20))
# print(cut_rod_recurision_2(p, 20))

# 解决方式
@cal_time
def c1(p, n):
    return cut_rod_recurision_1(p,n)

@cal_time
def c2(p, n):
    return cut_rod_recurision_2(p,n)

print(c1(p, 15))
print(c2(p, 15))
# 以上递归时间复杂度 O(2^n)

# 自底向上实现 ， 采用动态规划的思想
@cal_time
def cut_rot_dp(p, n):    # p是价格表
    r = [0]    # 长度是0的时候，收益就是0    0m  --  0yuan

    # 接下来要算 1m  2m  3m  ... rn米的收益
    for i in range(1, n+1):   # 下标代表几米    i == n   比n小的r都出来了
        res = 0
        for j in range(1, i+1):   # 几种情况
            res = max(res, p[j] + r[i-j])
        r.append(res)

    return r[n]

print(cut_rot_dp(p, 15))
# 时间复杂度： O(n^2)


