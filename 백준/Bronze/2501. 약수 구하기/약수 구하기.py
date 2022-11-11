n,k = map(int,input().split())
cnt =[]
for i in range(1,n+1):
    if n%i ==0:
        cnt.append(i)
if k>len(cnt):
    print(0)
else:
    print(cnt[k-1])