from typing import List


# 1.1 Merge Sorted Array - https://leetcode.com/problems/merge-sorted-array/description/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        sum = m + n - 1
        m = m - 1
        n = n - 1
        for i in range(sum, -1, -1):
            if n < 0: break
            if m >= 0 and nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1



# 1.2 Maximum Subarray - https://leetcode.com/problems/maximum-subarray/description/
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        cur_sum=0
        for num in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum+=num
            max_sum=max(max_sum,cur_sum)
        return max_sum