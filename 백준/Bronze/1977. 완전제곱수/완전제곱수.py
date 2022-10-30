m = int(input())
n = int(input())

cnt =0
b=1
a=[]
for i in range(m,n+1):
    t = int(i**0.5)**2
    if i ==t:
        a.append(i)
if a:
    print(sum(a))
    print(min(a))
else:
    print(-1)
