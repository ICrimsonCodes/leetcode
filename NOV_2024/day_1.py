# Question: https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/?envType=daily-question&envId=2024-11-01
# 1957. Delete Characters to Make Fancy String
# Time: O(n)
# Space: O(1)
class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []

        for char in s:
            # Check if the last two characters in the result are the same as the current character
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue  # Skip adding this character to avoid three consecutive identical characters
            result.append(char)

        return "".join(result)
