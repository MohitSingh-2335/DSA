s = list(input("String: "))
k = int(input("Window: "))

v = ['a','e','i','o','u']
st = s[0 : k]
cou = len([char for char in st if char in v])
tot = 0

if cou > tot:

    tot = cou

for i in range(k, len(s)):
  
    if s[i] in v:

        cou += 1

    if s[i - k] in v:

        cou -= 1

    if cou > tot:

        tot = cou

print(tot)

# for j in range(i + k, len(s) + 1):

#     cou += len([char for char in s[i : j] if char in v])

#     if cou > tot:

#         tot = cou

#     cou = 0

#     i += 1

# print(tot)