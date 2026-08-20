class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start = 0
        highLen = 0
        num = k
        strS = list(s)
        for end in range(start, len(s)):
            if strS[start] == strS[end] and num >= 0:
                highLen = len(strS[start : end + 1])
            elif strS[start] != strS[end] and num > 0:
                strS[end] = strS[start]
                highLen = len(strS[start : end + 1])
                num -= 1
            elif strS[start] != strS[end] and num == 0:
                break
        return highLen

s = input()
k = map(int, input())
obj = Solution()
ans = obj.characterReplacement(s, k)
print(ans)