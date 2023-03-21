n,m = map(int,input().split())
s=[]
p=[]
for _ in range(m):
    a,b = map(int,input().split())
    p.append(a)
    s.append(b)

min_p=min(p)

ans =0
while n>0:
    if n>=6:
        min_s = min(s)*6
        n-=6
    else:
        min_s= min(s)*n
        n-=n
    if min_s<min_p:
        ans+=min_s
    else:
        ans += min_p
print(ans)


            
