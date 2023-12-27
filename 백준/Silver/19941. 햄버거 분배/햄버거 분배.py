


N,K = map(int,input().split())
arr = list(input())
ans =0
for i in range(N):
    if arr[i] == 'P':
        # 해당 인덱스가 사람일 경우
        for i in range(max(i-K,0),min(i+K+1,N)):
            #K 범위 안에 있는 햄버거를 고른후 0 으로 처리            
            if arr[i] == 'H':
                arr[i] = 0
                ans +=1
                break
print(ans)