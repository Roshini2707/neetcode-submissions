class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        char_count = {}
        for right in range(len(s)):
            char_count[s[right]] = 1 + char_count.get(s[right], 0)
            max_f = max(char_count.values())
            window_length = right - left + 1
            if window_length - max_f <= k:
                max_length = max(max_length, right - left + 1)
            else:
                char_count[s[left]] -= 1
                left += 1
        return max_length




