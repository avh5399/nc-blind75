class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for char in range(len(s)):
            count_s[s[char]] = 1 + count_s.get(s[char], 0)
            count_t[t[char]] = 1 + count_t.get(t[char], 0)

        for char in count_s:
            if count_s[char] != count_t.get(char, 0):
                return False
        return True


