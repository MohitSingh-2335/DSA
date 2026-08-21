class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start = 0
        end = 0
        highLen = 0
        num = k
        strS = list(s)
        if len(s) < 0:
            return 0
        while (end < len(strS)):
            if strS[start] == strS[end] and num >= 0:
                highLen = len(strS[start : end + 1])
                end += 1
            elif strS[start] != strS[end] and num > 0:
                strS[end] = strS[start]
                highLen = len(strS[start : end + 1])
                num -= 1
                end += 1
            elif strS[start] != strS[end] and num == 0:
                start += 1
                end = start + 1
                num = k
                strS = list(s)
        return highLen

s = input()
k = map(int, input())
obj = Solution()
ans = obj.characterReplacement(s, k)
print(ans)