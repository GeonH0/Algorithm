





from collections import deque


n = int(input())
q = deque(range(1,n+1))

discard = [] #버린카드 저장

while len(q) > 1:
    discard.append(q.popleft()) #제일 위 카드 버리고
    q.append(q.popleft()) # 다음 카드 제이 ㄹ아래로 이동

discard.append(q[0])
print(*discard)

