nums = list(map(int, input("Array: ").split()))
k = int(input("Target: "))

res = sum(nums[0:k])
tot = 0
high = []
high.append(res/k)

for i in range(k, len(nums)):

    res += nums[i] - nums[i - k]

    high.append(res/k)

tot = max(high)

# while l <= len(nums) - tar:

#     r = (l + tar)

#     # for i in range(l, r):

#     #     res += nums[i]

#     tot = res/tar
    
#     if tot > high:

#         high = tot

#     l += 1

#     res = 0

print(tot, end = "")   