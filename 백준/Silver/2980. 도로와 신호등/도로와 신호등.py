


N,L = map(int,input().split())
pos =0 
ans =0
for _ in range(N):
    D,R,G = map(int,input().split())
    ans +=(D-pos)
    pos = D

    if ans %(R+G)<=R:        
        ans +=(R-(ans % (R+G)))
ans +=(L-pos)
print(ans)
