nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]

max_value = float('-inf')

# n = 0
# i = 0
# res = 0

# while n < len(nums):

#     #j = i + n
#     # res = nums[i : j + 1]

#     # if sum(res) > max_value:
#     #     max_value = sum(res)
#     if i + n < len(nums):

#         for j in range(i, i + n + 1):
#             res += nums[j]

#     else:

#         pass

#     if res > max_value:
#         max_value = res

#     i += 1
    
#     if i >= len(nums):
#         i = 0
#         n += 1
#     res = 0

# print(max_value)


# i = 0
# j = 3
# add = 0

# for n in range(i , j):
#     print(nums[n])

#     add += nums[n]

#     if add > max_value:
#         max_value = add

#for n in range(0, len(nums)):

#    for i in range(len(nums)):


# n = len(nums)

# for i in range(n):
#     res = 0

#     for j in range(i, n):
#         res += nums[j]

#         if res > max_value:
#             max_value = res

start = 0

for i in nums:
    if start < 0:
        start = 0
    start += i

    if start > max_value:
        max_value = start

print(max_value)