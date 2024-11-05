class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        while i < len(word):
            # Count consecutive characters, up to a maximum of 9
            count = 1
            while i + count < len(word) and word[i + count] == word[i] and count < 9:
                count += 1
            # Append the count and the character to comp
            comp += str(count) + word[i]
            # Move to the next group of characters
            i += count
        return comp
