# nums = [1,2,3,1]
# nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]
# nums = [0,4,5,0,3,6]

dic ={}
high = 0

for i in nums:
    if i in dic:

        dic[i] += 1
        high = dic[i]

    else:

        dic[i] = 1

# high = max(dic.values())

if high > 1:

    print('True')

else:

    print('False')
