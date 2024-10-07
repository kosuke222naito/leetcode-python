#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:  # type: ignore
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums and nums.index(complement) != i:
                return sorted([nums.index(complement), i])


# @lc code=end
