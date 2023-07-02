

m = list(input())
answer = []
tmp =[]

for i in range(1,len(m)-1):
    for j in range(i+1,len(m)):
        a = m[:i]
        b = m[i:j]
        c  = m[j:]
        a.reverse()
        b.reverse()
        c.reverse()        
        tmp.append(a+b+c)

for k in tmp:
    answer.append(''.join(k))

print(sorted(answer)[0])
