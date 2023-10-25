

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())

ans = N
for n in A:
    if n - B >0:
        ans += (n- B + C -1)//C
print(ans)
    
        
        

