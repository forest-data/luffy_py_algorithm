"""
1. 给两个字符串s 和 t, 判断t是否为s的重新排列后组成的单词
s = 'anagram'  ,  t = 'nagaram', return true
s = 'rat', t='car', return false
"""
class Solution:

    def isAnagram1(self, s, t):
        ss = list(s)
        tt = list(t)

        ss.sort()
        tt.sort()

        return ss==tt

    #
    def isAnagram2(self, s, t):
        return sorted(list(s))==sorted(list(t))

    # 时间复杂度 O(n)
    def isAnagram3(self, s, t):
        # 思路: 统计字母的数量

        dict1 = {}    # 'a':1   'b':2
        dict2 = {}

        for ch in s:
            dict1[ch] = dict1.get(ch, 0) + 1

        for ch in t:
            dict2[ch] = dict2.get(ch, 0) + 1

        return dict1 == dict2


# print(Solution().isAnagram1('abca', 'acba'))
#
# print(Solution().isAnagram2('abca', 'acba'))

print(Solution().isAnagram3('abca', 'acba'))
