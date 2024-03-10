N, M = map(int, input().split())
score = list(map(int, input().split()))

ms = 0
mi = float('inf')  # 무한대로 초기화하여 모든 숫자보다 크게 설정

for _ in range(M):
    arr = input().split()
    s = sum(score[i - 1] for i in range(1, len(arr)) if arr[i] == 'O')
    
    if s > ms:
        ms = s
        mi = int(arr[0])  # 숫자로 변환하여 비교
    elif s == ms:
        mi = min(mi, int(arr[0]))  # 숫자로 변환하여 비교

print(mi, ms)
