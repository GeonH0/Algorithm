t= int(input())
cnt =0
for i in range(t):
    n,m = map(int,input().split())
    while n<=m:
        for j in str(n):
            if j =='0':
                cnt +=1
        n+=1
    print(cnt)
    cnt =0