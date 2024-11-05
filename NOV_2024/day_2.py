# Question: https://leetcode.com/problems/circular-sentence/description/?envType=daily-question&envId=2024-11-02
# 2490. Circular Sentence
# Time: O(n)
# Space: O(1)
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i in range(len(words)):
            current_word = words[i]
            next_word = words[(i + 1) % len(words)]

            if current_word[-1] != next_word[0]:
                return False

        return True
