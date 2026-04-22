class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            current_char = s[right]
            while current_char in seen_chars:
                seen_chars.remove(s[left])
                left += 1
            seen_chars.add(current_char)
            max_length = max(max_length, right-left+1)
        return max_length

        