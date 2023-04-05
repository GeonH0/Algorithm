import itertools


n,d = map(int,input().split())
arr =[]
cnt =0
for i in range(1,n+1):
    arr.append(list(map(int,str(i))))
arr = list(itertools.chain(*arr))

for i in arr:
    if i ==d:
        cnt +=1
print(cnt)



