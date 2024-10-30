
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    s = 0

    ans = 0
    while s < N:
        i_max = s
        for i in range(s+1,N):
            if arr[i_max] < arr[i]:
                i_max = i
        for i in range(s,i_max):
            ans += (arr[i_max] - arr[i])
        s = i_max+1



    print(f"#{test_case} {ans}")