# nums = [2,2,1]
nums = [4,1,2,1,2]

dic = {}
high = []

for i in nums:
    if i in dic:

        dic[i] += 1

    else:

        dic[i] = 1

print(dic)

a = [j for j, k in dic.items() if k == 1]

print(a)
print("".join(map(str, a)))
