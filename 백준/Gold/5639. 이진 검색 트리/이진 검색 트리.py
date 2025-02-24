

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
arr = []

while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break

def solution(lst):
    if len(lst) == 0:
        return
    
    l,r = [],[]
    mid= lst[0]
    for i in range(1,len(lst)):
        if lst[i]>mid:
            l = lst[1:i]
            r = lst[i:]
            break
    else:
        l = lst[1:]
    solution(l)
    solution(r)
    print(mid)

solution(arr)
