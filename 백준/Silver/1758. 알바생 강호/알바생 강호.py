n = int(input())

tip = []

for i in range(n):
    tip.append(int(input()))

tip.sort(reverse=True)

for j in range(n):
    if tip[j]-j>0:
        tip[j] =tip[j]-j
    else:
        tip[j]=0
print(sum(tip))