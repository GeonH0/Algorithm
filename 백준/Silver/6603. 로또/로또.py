def dfs(n,s,lst):
    if n == 6:
        ans.append(lst)
        return

    for j in range(s,len(arr)):
        if v[j]==0:   
            v[j]=1
            dfs(n+1,j+1,lst+[arr[j]])
            v[j]=0
        
        


        



while True:
    
    arr=list(map(int,input().split()))
    if arr[0]==0:
        break
    k = arr.pop(0)
    v=[0]*len(arr)
    ans =[]
    dfs(0,0,[])
    for i in ans:
        print(*i)
    print()