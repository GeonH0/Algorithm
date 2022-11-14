n = int(input())
p = [[0]*101 for i in range(101)]

for j in range(n):
    a,b = map(int,input().split())
    for i in range(10):
        for k in range(10):
            p[a+i][b+k] =1

r=0
for i in p:
    r +=sum(i)
print(r)

