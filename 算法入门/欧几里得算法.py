# 最大公约数  12  16  最大公约数是 4

# 欧几里得： 辗转相除法

# 欧几里得算法：  gcd(a, b) = gcd(b, a mod b)

# 尾递归： 如果一个函数中所有递归形式的调用都出现在函数的末尾，我们称这个递归函数是尾递归的
# 尾递归的效率跟循环是一样的。
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(12, 16))


# 非递归实现欧几里得算法
def gcd2(a,b):
    while b > 0:
        r = a % b
        a, b = b, r
    return a

print(gcd2(12, 16))

# 实现分数计算
# 利⽤用欧⼏几⾥里里得算法实现⼀一个分数类，⽀支持分数的四则运算
# 分数 Fraction
class Fraction:

    def __init__(self, a, b):
        self.a = a
        self.b = b

        x = self.gcd(a, b)
        self.a /= x
        self.b /= x

    @staticmethod
    def gcd(a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    # 最小公倍数
    @staticmethod
    def zxgbs(a,b):
        # 12 16  -> 4
        # 3 * 4 * 4 = 48    12/4 = 3    16/4 = 4   4最大公约数
        x = gcd(a,b) # 最大公约数
        return a * b / x


    def __add__(self, other):   # other 是Fraction对象
        # 1/12 + 1/20
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        fenmu = self.zxgbs(b, d)   # 分母
        fenzi = a * (fenmu/b) + c * (fenmu/d)   # 分子

        return Fraction(fenzi, fenmu)




    def __str__(self):
        return "%d/%d" %(self.a, self.b)

# 测试约分
f = Fraction(30, 16)
print(f)

a = Fraction(16, 30)
b = Fraction(5, 12)
print(a, b)
print(a + b)
