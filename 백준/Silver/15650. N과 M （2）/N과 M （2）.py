


def dfs(n,lst):

    #종료 조건
    if n > N:
        if len(lst) == M: #길이가 M이 되면
            ans.append(lst)
        return
    dfs(n+1,lst+[n]) # 선택
    dfs(n+1,lst)# 선택 하지 않을 경우
    





N,M = map(int,input().split())


ans=[]
dfs(1,[])
for i in ans:
    print(*i)
