n = int(input())
arr = map(int, input().split())

ar = list(arr)

if len(list(ar)) != n:
    print("Invalid")

res = sorted(set(ar))

print(res)

print(list(res)[-2])