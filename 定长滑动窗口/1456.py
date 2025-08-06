class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # yy=set(["a","e","i","o","u"])
        res = 0
        maxres = -1
        right = 0
        while right < len(s):

            left = right - k + 1
            if s[right] in "aeiou":
                res += 1
            maxres = max(res, maxres)
            if left < 0:
                right += 1
                continue
            if s[left] in "aeiou":
                res -= 1
            maxres = max(res, maxres)
            right += 1
        return maxres
