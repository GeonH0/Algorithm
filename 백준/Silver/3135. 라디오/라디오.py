a,b = map(int,input().split())
n = int(input())

c=[]
s1 = abs(a-b)
for i in range(n):
   c.append(int(input()))

for i in range(len(c)):
    s1 = min(s1,abs(c[i]-b)+1)

print(s1)