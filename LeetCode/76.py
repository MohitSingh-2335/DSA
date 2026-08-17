class Solution:
    def minWindow(self, s: str, t: str) -> str:

        i = 0
        temp = list(t)
        count = 0
        for j in range(len(s)):
            a = s[i : j]
            for k in range(len(a)):
                for m in range(len(temp)):
                    if a[k] == temp[m]:
                        temp.remove(a[k])
            if temp == []:
                count = a
                break
        else:
            j += 1

        return count

s = input()
t = input()
obj = Solution()
ans = obj.minWindow(s,t)
print(ans)