from typing import List


# 3.1 Word Pattern - https://leetcode.com/problems/word-pattern/description/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if not len(words) == len(pattern): return False
        words_m = dict()
        letters_m = dict()
        for i in range(len(pattern)):
            if not letters_m.setdefault(pattern[i], words[i]) == words[i]:
                return False
            if not words_m.setdefault(words[i], pattern[i]) == pattern[i]:
                return False
        return True

# 3.2 Two Sum - https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i in range(len(nums)):
            map.setdefault(nums[i], i)
        print(not map.get(6 - 2) == None)
        for i in range(len(nums)):
            mapidx = map.get(target - nums[i])
            if not mapidx == None and not mapidx == i:
                return [i, map.get(target - nums[i])]