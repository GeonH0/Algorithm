from itertools import permutations


n = int(input())
k= int(input())
a= []
for i in range(n):
    a.append(input())
res = set()
for per in permutations(a,k):
    res.add(''.join(per))

print(len(res))