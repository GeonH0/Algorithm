n = int(input())
lit=list(map(int,input().split()))
cnt = 0
lit.sort(reverse=True)
for i in range(n):
    if i==0:
        cnt += lit[i]
    else:
        cnt += lit[i]/2

print(cnt)