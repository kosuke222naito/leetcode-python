#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        x_str = f"{x}"
        x_str_reversed = x_str[::-1]
        if x_str == x_str_reversed:
            return True
        else:
            return False


# @lc code=end
