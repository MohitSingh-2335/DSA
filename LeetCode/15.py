class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        count = []
        i = 0
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    count.append([i,j,k])
        else:
            i += 1
        return count

nums = list(map(int, input().split()))
obj = Solution()
ans = obj.threeSum(nums)
print(ans)