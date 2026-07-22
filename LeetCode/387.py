s = list(input('String: '))

dic = {}
non = []
high = 0

for i in s:

    if i not in non:

        if i not in dic:

            dic[i] = s.index(i)

        elif i in dic:

            non += i
            del dic[i]

    if len(dic) == 0:

        print('-1')

print(list(dic.values())[0])

# high = list(dic.values())
# j = 1

# if j in high:

#     print(s.index(j))

# else:

#     print('-1')