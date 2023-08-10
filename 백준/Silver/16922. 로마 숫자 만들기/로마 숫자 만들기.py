from itertools import combinations, combinations_with_replacement

n = int(input())
num = [1, 5, 10, 50]
ans = []

for temp in combinations_with_replacement(range(4),n):
    sum =0
    for i in temp:
        sum += num[i]
    ans.append(sum)
print(len(set(ans)))
