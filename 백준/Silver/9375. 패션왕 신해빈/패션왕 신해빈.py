


from typing import Counter


T = int(input())
for _ in range(T):
    n = int(input())
    w = []
    for _ in range(n):
        c,type = map(str,input().split())
        w.append(type)
    w_C = Counter(w)
    cnt = 1

    for k in w_C:
        cnt *=w_C[k] +1
    print(cnt-1)
        