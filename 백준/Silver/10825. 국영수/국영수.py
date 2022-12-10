



n = int(input())
arr=[]
for i in range(n):
    name,k,e,m = list(map(str,input().split()))
    arr.append([name,int(k),int(e),int(m)])
arr.sort(key = lambda x : (-x[1],x[2],-x[3],x[0]))

for j in arr:
    print(j[0])