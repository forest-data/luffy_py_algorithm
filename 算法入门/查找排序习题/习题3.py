"""
3. 给 nums =【1，2，5，4】 target = 3   结果 返回  （0，1）
"""
from 算法入门.cal_time import cal_time


class Solution:

    @cal_time
    def twoSum1(self, nums, target):
        for ind, val in enumerate(nums):
            if target - val in nums and ind != nums.index(target-val):
                return (ind, nums.index(target-val))

    # 前一个数 和 后面的数比
    @cal_time
    def twoSum2(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):   # 跟后面的比      # 跟前面的比 for j in range(i)
                if nums[i] + nums[j] == target:
                    return sorted([i, j])


    def binary_search(self, li, left, right, val):

        # left = 0
        # right = len(li)-1

        while left <= right:
            mid = (left + right) // 2

            if li[mid] == val:
                return mid
            elif li[mid] > val:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return None

    # 假如列表是有序的， 查找 val - target 可采用二分查找
    @cal_time
    def twoSum3(self, nums, target):
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b>=a:
                # j = self.binary_search(nums[i+1:], b)  # 列表切片复杂度O(n)
                j = self.binary_search(nums, i+1, len(nums)-1, b)
            else:
                j = self.binary_search(nums, 0, i-1, b)
            if j:
                break

        return sorted([i,j])


    def binary_search2(self, li, left, right, val):

        # left = 0
        # right = len(li)-1

        while left <= right:
            mid = (left + right) // 2

            if li[mid][0] == val:
                return mid
            elif li[mid][0] > val:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return None
    @cal_time
    def twoSum4(self, nums, target):

        new_nums = [[num, i] for i, num in enumerate(nums)]
        new_nums.sort(key= lambda x:x[0])


        for i in range(len(new_nums)):
            a = new_nums[i][0]
            b = target - a
            if b >= a:
                # j = self.binary_search(nums[i+1:], b)  # 列表切片复杂度O(n)
                j = self.binary_search2(new_nums, i + 1, len(new_nums) - 1, b)
            else:
                j = self.binary_search2(new_nums, 0, i - 1, b)
            if j:
                break

        return sorted([new_nums[i][1], new_nums[j][1]])


nums = [1,2,4,5]
target = 3
print(Solution().twoSum1(nums, target))
print(Solution().twoSum2(nums, target))
print(Solution().twoSum3(nums, target))
print(Solution().twoSum4(nums, target))