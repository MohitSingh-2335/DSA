class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ascii_val = [0] * 26
        for i in strs:
            j = 0
            ascii_val[ord(i[j]) - ord('a')] += 1
            j += 1
        return ascii_val
            

strs = input().split()
obj = Solution()
ans = obj.groupAnagrams(strs)
print(ans)