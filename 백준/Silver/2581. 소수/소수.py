
n = int(input())
m = int(input())

sosu = []

for i in range(n,m+1):
    e = 0
    if i>1:
        for j in range(2,i):
            if i%j ==0:
                e +=1
                break
        if e == 0:
            sosu.append(i)

if len(sosu)>0:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)