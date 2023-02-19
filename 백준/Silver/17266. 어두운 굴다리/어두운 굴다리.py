import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
x= list(map(int,input().split()))
l = len(x)
h = 0

if l ==1:
    h = max(x[0]-0,n-x[0])
else:
    for i in range(l):
        if i==0:
            height = x[i]-0
        elif i == l-1:
            height = n-x[i]
        else:
            tmp = x[i]-x[i-1]
            if tmp%2:
                height = tmp //2 +1
            else:
                height = tmp //2
        h = max(height,h)
print(h)
