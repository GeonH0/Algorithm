
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    ans =0
    arr = arr[::-1]
    mx = 0
    for n in arr:
        if mx < n:
            mx = n
        else:
            ans += (mx - n)



    print(f"#{test_case} {ans}")