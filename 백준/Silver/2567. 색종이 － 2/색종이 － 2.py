
from itertools import count


n = int(input())
p = [[0]*101 for _ in range(101)]


def count(arr):
    cnt =0
    for lst in arr:
        for i in range(1,len(lst)):
            if lst[i-1] != lst[i]:
                cnt +=1
    return cnt

for j in range(n):
    a,b = map(int,input().split())
    for i in range(10):
        for k in range(10):
            p[a+i][b+k]=1
            #해당 영역 1로 표시
p_t= list(zip(*p))
ans = count(p) + count(p_t)

print(ans)
