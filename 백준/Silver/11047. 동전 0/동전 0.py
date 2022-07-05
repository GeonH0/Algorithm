import sys

input = sys.stdin.readline

n,k=map(int,input().split())
a=list()
for i in range(n):
    a.append(int(input()))
c=0
for i in reversed(range(n)):
    c+=k//a[i]
    k= k%a[i]
print(c)