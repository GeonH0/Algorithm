

N,K = map(int,input().split())
p =0
cnt =0
arr = []
for _ in range(N):
    arr.append(int(input()))


for i in range(N):
    t = arr[p]
    cnt +=1
    if t == K:
        print(cnt)
        break
    else:
        p = t
else:
    print(-1)