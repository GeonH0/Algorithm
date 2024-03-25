import sys
input = sys.stdin.readline

N,Q = map(int,input().split())

v = [0] * (N+1)

for _ in range(Q):
    x = int(input())
    target = x
    flag = 0

    while target !=1:

        if v[target] >=1:
            flag = target
        
        target //=2
    
    if flag:
        print(flag)
    else:
        v[x] = 1
        print(0)
