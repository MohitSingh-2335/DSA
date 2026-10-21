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
        sorted_list = []
        sorted_dic = {}
        anagram_dic = {}
        for element in strs:
            anagram_dic[element] = "".join(sorted(element))
        for dic_key, dic_value in anagram_dic.items():
            if dic_value not in sorted_dic:
                sorted_dic[dic_value] = []
            sorted_dic[dic_value].append(dic_key)
        sorted_list = list(sorted_dic.values())
        if len(strs) == 0:
            return strs
        return sorted_list


strs = input().split()
obj = Solution()
ans = obj.groupAnagrams(strs)
print(ans)