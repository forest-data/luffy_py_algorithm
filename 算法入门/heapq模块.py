# python内置模块 heapq
# 堆的特性: 优先队列
import random
import heapq     # heap queue 优先队列 小的先出，或者大的先出   队列 先进先出

li = list(range(100))
random.shuffle(li)
print(li)

heapq.heapify(li)    # 建堆
heapq.heappop(li)    # 往外弹元素
print(li)

# print(heapq.heappop(li))
# print(heapq.heappop(li))

