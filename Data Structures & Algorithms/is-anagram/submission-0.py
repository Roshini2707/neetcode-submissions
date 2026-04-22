class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_list = list(s)
            t_list = list(t)
            s_list.sort()
            t_list.sort()
            if s_list == t_list:
                return True
        return False
        