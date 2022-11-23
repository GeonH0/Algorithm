

n = int(input())
m = list(map(int,input().split()))
h = list(map(int,input().split()))

pl = [0 for _ in range(101)]

for i in range(1,n+1):
    s = m[i-1]
    p = h[i-1]
    for j in range(100,0,-1):
        if j>s:
            pl[j]=max(pl[j],pl[j-s]+p)
print(pl[-1])