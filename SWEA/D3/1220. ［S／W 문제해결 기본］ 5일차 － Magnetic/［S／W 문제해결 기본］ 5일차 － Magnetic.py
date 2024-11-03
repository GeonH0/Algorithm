

#빈칸은 무시, 1,2의 경우, 2를 찾고 , 직전값이 1인 경우 -> 교착상태
#직전 색을 갱신 -> prev

T = 10
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    #전치 행렬로 생성 -> 세로 방향으로 탐색하기 위해
    arr1 = list(zip(*arr))
    for lst in arr1:
        prev = 0
        for n in lst:
            if n:
                if n ==2 and prev == 1:
                    ans +=1
                prev = n
    print(f"#{test_case} {ans}")



