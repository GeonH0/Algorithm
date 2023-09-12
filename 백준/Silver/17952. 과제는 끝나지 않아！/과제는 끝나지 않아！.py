



N = int(input())
a=[]
s=[]
cnt =0
for i in range(N):
    a=list(map(int,input().split()))

    if a[0]==1:
        s.append((a[1],a[2]))

    if s:
        a,b = s.pop()
        b -=1
        if b==0:
            cnt +=a
        else:
            s.append((a,b))

print(cnt)

