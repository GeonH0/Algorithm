





import heapq


N = int(input())
T = int(input())
arr=list(map(int,input().split()))
s={}
for i in arr:
    if i not in s:
        if len(s) >=N:
            a = heapq.nsmallest(min(s),s,key =s.get)
            s.pop(a[0])
        s[i]=1
    else:
        s[i] +=1

print(*sorted(s.keys()))