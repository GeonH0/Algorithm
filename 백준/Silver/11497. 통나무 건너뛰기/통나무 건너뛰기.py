import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    s.sort()
    r = 0
    for j in range(2,n):
        r = max(r,abs(s[j]-s[j-2]))
    print(r)