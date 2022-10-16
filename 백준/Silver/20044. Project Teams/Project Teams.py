n = int(input())

a=list(map(int,input().split()))

a.sort()
s=[]
for i in range(n):
    s.append(a[i]+a[len(a)-i-1])
s.sort()
print(s[0])