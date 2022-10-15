n,m = map(int,input().split())

p=[]
price = 0
totla =0
for i in range(m):
    p.append(int(input()))

p.sort(reverse=True)
for j in range(m):
    if j +1>n:
        profit = p[j]*n
    else:
        profit=p[j]*(j+1)
    if totla <profit:
        price=p[j]
        totla=profit

print(price,totla)