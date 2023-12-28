







from collections import Counter


while True:
    ans = []
    arr=[]

    N,M = map(int,input().split())
    if N ==0 and M ==0:
        break
    
    for _ in range(N):
        arr += list(map(int,input().split()))
        
        #카운트 하고 내림차순으로 정렬
    arr_count =sorted(Counter(arr).items(), key = lambda x : x[1],reverse=True)
    ans.append(arr_count[1][0])
    #동점자가 있다면 동점자도 입력

    for i in range(2,len(arr_count)):
        if arr_count[i][1] != arr_count[1][1]:
            break
        else:
           ans.append(arr_count[i][0])
        
    print(*sorted(ans))
