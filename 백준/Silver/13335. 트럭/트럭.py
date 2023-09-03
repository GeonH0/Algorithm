








n,w,l = map(int,input().split())
t = list(map(int,input().split()))

b=[0]*w
cnt =0

while b:
    cnt +=1
    b.pop(0)
    if t:
        if sum(b) + t[0]<=l:
            b.append(t.pop(0))
        else:
            b.append(0)
print(cnt)
    
    