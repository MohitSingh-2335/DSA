arr = []

for _ in range(int(input())):

    name = input()
    score = float(input())

    arr.append([name, score])

print(arr)

ar = sorted(arr, key = lambda i : i[1])

for j in ar:

    if j[1] == ar[i][1]: