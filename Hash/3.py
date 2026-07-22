class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        a = list(s)
        count = []
        i = 0
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                i += 1
            else:
                count.append(a[j])
        return len(count)


s = input()
obj = Solution()
ans = obj.lengthOfLongestSubstring(s)
print(ans)