"""
#查找一个数是否在 二维列表中
"""
class Solution:

    # 思路：变现的线性查找
    def isAnagram1(self, matrix, target):

        # O(m*n)   列表长m 宽n
        for line in matrix:
            if target in line:   # 对于列表执行in 时间复杂度 O(n)
                return True
        return False

    # 思路：二分查找
    def isAnagram2(self, matrix, target):

        h = len(matrix)   # 行
        w = len(matrix[0])   # 列

        left = 0
        right = w * h - 1

        while left <= right:     # 候选区有值
            mid = (left + right) // 2  # 对2进行整除，向下取整
            i = mid // w   # 行
            j = mid % w    # 列

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return False


matrix = [[1,3,5], [7,8,9]]
target = 8
print(Solution().isAnagram2(matrix, target))

