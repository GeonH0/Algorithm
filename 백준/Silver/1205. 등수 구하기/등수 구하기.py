


N,T,P = map(int,input().split())


if N ==0: #랭킹이 아예 등록이 안되어있을경우
    print(1)
else:    
    arr=list(map(int,input().split()))
    if N==P and min(arr)>=T:# 랭킹리스트에 올라갈수 없을정도로 낮을경우(단 N과 P)
        print(-1)
    else:
        ans = N+1 #갱신되는 경우
        for i in range(N):
            if arr[i]<=T:
                ans = i+1
                break
        print(ans)
                
                
                

            