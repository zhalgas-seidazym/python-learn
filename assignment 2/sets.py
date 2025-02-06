from typing import List


# 2.1 Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setik = set()
        setik_len = 0
        for n in nums:
            setik.add(n)
            if(not len(setik) == setik_len):
                setik_len = len(setik)
            else: return True
        return False


# 2.2 Intersection of Two Arrays -
# https://leetcode.com/problems/intersection-of-two-arrays/description/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = set()
        check = set()
        for n in nums1:
            check.add(n)
        check_len = len(check)
        for n in nums2:
            check.add(n)
            if(check_len == len(check)):
                inter.add(n)
            else: check.remove(n)
        return list(inter)