
# 백트래킹 ->  가능한 모든 경우
# n 선택할 숫자, 종료 조건을 명확하게 하자 조건 n>N
# lst 숫자 선택 변수

def dfs(n,lst):
    # 종료 조건
    if n > N:
        if len(lst) == M:
            ans.append(lst)
        return
    #하부 함수 호출 2가지
    
    # 선택한 경우
    dfs(n+1,lst+[n])
    # 선택하지 않은 경우
    dfs(n+1,lst)


ans =[]
N,M = map(int,input().split())
dfs(1,[])
for i in ans:
    print(*i)