


def dfs(n,cnt,lst):
    #n: 배열의 index, cnt 모음의 갯수
    if n == C:
        # 비밀번호 길이, 모음,자음갯수 확인
        if len(lst)==L and cnt >=1 and L-cnt>=2:
            ans.append(lst)        
        return
        
    #포함하는 경우
    dfs(n+1,cnt+tbl[ord(arr[n])],lst+arr[n])
    #포함하지 않는 경우
    dfs(n+1,cnt,lst)





    



L,C = map(int,input().split())

arr= sorted(input().split())

#lookuptable 모음인경우 1, 아닌경우 0
tbl=[0]*128

for j in "aeiou":
    tbl[ord(j)]=1

ans =[]
dfs(0,0,"")

for i in ans:
    print(i)