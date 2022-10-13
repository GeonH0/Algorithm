t = int(input())

for i in range(t):
    j,n = map(int,input().split())
    s=[]
    for i in range(n):
        a=list(map(int,input().split()))
        s.append(a[0]*a[1])
    s.sort(reverse=True)
    cnt =0
    for k in range(len(s)):
        j-=s[k]
        cnt +=1
        if j<=0:
            break
    print(cnt)