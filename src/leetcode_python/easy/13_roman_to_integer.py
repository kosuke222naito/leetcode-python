#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    ROMAN: dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        answer = 0
        for i, char in enumerate(s):
            digit: int = self.ROMAN[char]
            if i == len(s) - 1:
                answer += digit
            elif self.ROMAN[char] < self.ROMAN[s[i + 1]]:
                answer -= digit
            else:
                answer += digit
        return answer


# @lc code=end
