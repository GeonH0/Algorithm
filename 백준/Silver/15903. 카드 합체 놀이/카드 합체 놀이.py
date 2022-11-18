n,k= map(int,input().split())
a = list(map(int,input().split()))
for i in range(k):
    a = sorted(a)
    c = a[0]+a[1]
    a[0]=c
    a[1]=c
print(sum(a))