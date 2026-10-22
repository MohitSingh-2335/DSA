class Solution:
    def oldgroupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ascii_val = [0] * 26
        for i in strs:
            j = 0
            num = ascii_val[ord(i[j]) - ord('a')]
            if num != 0:
                j += 1
            else:
                num += 1
        return ascii_val

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 0:
            return strs
        sorted_dic = {}
        for element in strs:
            value = "".join(sorted(element))
            if value not in sorted_dic:
                sorted_dic[value] = []
            sorted_dic[value].append(element) 
        return list(sorted_dic.values())


strs = input().split()
obj = Solution()
ans = obj.groupAnagrams(strs)
print(ans)