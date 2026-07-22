import itertools

x = int(input())
y = int(input())
z = int(input())
n = int(input())

num = [x, y, z]

ran = [range(x + 1), range(y + 1), range(z + 1)]

res = [i for i in itertools.product(*ran) if sum(i) != n]

ress = [list(j) for j in res]

print(ress)