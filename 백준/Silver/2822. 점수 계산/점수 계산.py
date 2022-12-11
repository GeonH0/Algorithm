a=[]

cnt = 0 
for i in range(8):
    a.append(int(input()))

b=sorted(a,reverse=True)    
bi=[]
for i in b[:5]:
    bi.append(a.index(i)+1)

print(sum(b[:5]))
bi.sort()
print(*bi)