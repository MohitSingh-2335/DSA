height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
# height = [4,3,2,1,4]
# height = [2,3,4,5,18,17,6]

count = 0

i = 0
j = -1

while (i < len(height) and j >= -(len(height))):

    mini = min(height[i], height[j])

    res = mini * (abs(len(height) + j - i))

    if res >= count:

        count = res

    if height[i] > height[j]:

        j -= 1
    
    else:

        i += 1

print(count)

# for j in range(len(height)-1,-1,-1):

#     if height[i] * height[j] > count:

#         count = height[i] * height[j]
        
#         i += 1

#     else:

#         j -= 1

# print(count)



# h = sorted(height)
# a = h[-1]
# b = 0

# if len(h) <= 2:

#     print(h[0] * h[1])

# else:
    
#     for i in range(len(h)-1,-1,-1):

#         if h[i] != h[-1]:

#             b = h[i]
#             break

#     print((a - 1) * b)