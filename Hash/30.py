class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:

        import itertools

        a = []

        ans = list(itertools.permutations(words))

        for i in ans:
            ind = s.find(''.join(i))
            if ind != -1:
                a.append(ind)
        a.sort()

        return a

s = input( )
words = input( ).split()
obj = Solution()
ans = obj.findSubstring(s, words)
print(ans)