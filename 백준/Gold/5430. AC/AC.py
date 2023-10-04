from collections import deque


T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = input().rstrip()
    dq = deque(arr[1:-1].split(','))

    if n ==0:
        dq = deque()
    R =0
    for i in range(len(p)):
        if p[i] == 'R': #R의 횟수 찾기
            R +=1
        elif p[i] == 'D': # D 횟수
            if len(dq) ==0:
                print("error")
                break
            else:
                if R % 2 ==0: # R이 짝수 일경우 마지막 숫자를 빼내고
                    dq.popleft()
                else:
                    dq.pop() # R이 홀수일 경우 맨 앞자리를 제거

    else:
        if R % 2 == 0:
            print("[" + ",".join(dq) + "]")
        else:
            dq.reverse()
            print("[" + ",".join(dq) + "]")