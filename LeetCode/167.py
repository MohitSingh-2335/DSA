# nums = [2,7,11,15]
# tar = 9

# nums = [2,3,4]
# tar = 6

nums = [5,25,75]
tar = 100

l = 0
r = len(nums) - 1

while l < r:

    if nums[l] + nums[r] > tar:

        r -= 1

    elif nums[l] + nums[r] < tar:

        l += 1

    elif nums[l] + nums[r] == tar:

        print(l + 1, r + 1)
        break



# import itertools as it

# for i, j in it.combinations(enumerate(nums), 2):

#     if i[1] + j[1] == tar:

#         print(i[0] + 1, j[0] + 1)


# l = 0

# for r in range(l + 1, len(nums)):

#     if r <= len(nums):

#         if nums[l] + nums[r] == tar:

#             print(l + 1, r + 1)
            
#             l += 1


# l = 0
# r = l + 1

# if r <= len(nums):

#     if r <= len(nums):

#         print(l + 1, r + 1)

#     else:

#         l += 1

# for i in range(len(num)):

#     for j in range(1, len(num)):

#         if num[i] + num[j] == tar:

#             print (i + 1, j + 1)