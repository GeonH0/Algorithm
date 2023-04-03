
import sys
input = sys.stdin.readline

def m_sort(L):
    if len(L)==1:
        return L

    mid = (len(L)+1)//2

    

    i,j =0,0
    l2=[]

    l = m_sort(L[:mid])
    r = m_sort(L[mid:])

    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            l2.append(l[i])
            ans.append(l[i])
            i+=1
        else:
            l2.append(r[j])
            ans.append(r[j])
            j+=1
    while i<len(l):
        l2.append(l[i])
        ans.append(l[i])
        i+=1
    while j< len(r):
        l2.append(r[j])
        ans.append(r[j])
        j+=1

    return l2

        

    




cnt =1
a,k = map(int,input().split())

arr= list(map(int,input().split()))
ans=[]
m_sort(arr)

if len(ans)>=k:
    print(ans[k-1])
else:
    print(-1)