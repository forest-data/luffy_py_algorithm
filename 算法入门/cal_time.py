# 装饰器： 函数嵌套函数
# 闭包： 内部函数引用外部函数的变量
# 如何在内部函数中更改外部函数的变量， nonlocal
import time

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print('%s running time: %s secs.' % (func.__name__, t2-t1))
        return result

    return wrapper