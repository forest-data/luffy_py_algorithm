
# 栈: 是一个数据集合，只能在一段进行插入或删除操作

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    # 删除栈顶元素
    def pop(self):
        return self.stack.pop()

    # 获取栈顶元素
    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.get_top())   # 3
print(stack.pop())   # 3

# 匹配字符串问题
#

def brace_match(s):
    match = {')':'(', ']':'[', '}':'{'}
    stack = Stack()
    for ch in s:
        if ch in {'(','[','{'}:
            stack.push(ch)
        else:
            if stack.get_top() == match[ch]:   # ({}[])
                stack.pop()
            elif stack.is_empty():    # 首次进来的是  ] ) }
                return False
            elif stack.get_top() != match[ch]:    # ({)}
                return False

    if stack.is_empty():   #解决无结尾情况  ({}[]
        return True
    else:
        return False

print(brace_match('{{}()[]}'))


