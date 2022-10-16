
n = int(input())
a=[]
cnt =0
for i in range(n):
    a.append(int(input()))

for i in range(n-1,0,-1):
    if a[i]<=a[i-1]:
        cnt +=(a[i-1]-a[i]+1)
        a[i-1]=a[i] -1
print(cnt)