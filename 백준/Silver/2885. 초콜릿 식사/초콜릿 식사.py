import sys
input = sys.stdin.readline

K = int(input())
size,cnt = 0,0
for i in range(K):
    if K <= (2**i):
        size = (2**i)
        break
ans = size


while K>0:
    if K >= size:
        K = K-size
    else:
        size //=2
        cnt +=1

print(ans,cnt)