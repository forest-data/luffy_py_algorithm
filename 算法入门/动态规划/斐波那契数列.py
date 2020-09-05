# 动态规划： 是一种算法思想，算法套路。 基因匹对，序列的相似程度。

# 斐波那契数列

# 递归实现 > 问题 子问题重复计算
def fibnacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibnacci(n-1) + fibnacci(n-2)

# print(fibnacci(10))
# f(6) = f(5) + f(4)
# f(5) = f(4) + f(3)
# f(4) = f(3) + f(2)
# f(3) = f(2) + f(1)
# f(2) = 1

# 非递归实现  >  动态规划(DP)的思想 : 递归式
def fibnacci_no_recurision(n):
    f = [0, 1, 1]   # 第1项是1 ，第二项是1
    if n>2:
        for i in range(n-2):
            num = f[-1] + f[-2]
            f.append(num)

    return f[n]

# print(fibnacci_no_recurision(100))

# 递归执行效率低
# 递归使用时间比非递归要长原因： 递归子问题重复计算
