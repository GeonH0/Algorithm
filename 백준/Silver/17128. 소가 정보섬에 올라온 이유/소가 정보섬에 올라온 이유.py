def initial_S(cow, N):
    S = 0
    for i in range(N):
        # 각 i를 시작으로 연속한 네 마리의 소에 대한 곱셈
        S += cow[i] * cow[(i + 1) % N] * cow[(i + 2) % N] * cow[(i + 3) % N]
    return S

def update_S(cow, idx, N, S):
    # 선택된 소가 속한 4개의 곱셈을 업데이트해야 한다.
    # idx-3 ~ idx 위치에 해당하는 부분만 다시 계산
    
    # 선택된 소의 값을 반전시키기 전에 먼저 기존 값을 빼줍니다.
    for j in range(4):
        start_idx = (idx - j) % N
        S -= cow[start_idx] * cow[(start_idx + 1) % N] * cow[(start_idx + 2) % N] * cow[(start_idx + 3) % N]
    
    # 소의 값을 반전시킴
    cow[idx] *= -1
    
    # 새로 바뀐 값으로 다시 더해줌
    for j in range(4):
        start_idx = (idx - j) % N
        S += cow[start_idx] * cow[(start_idx + 1) % N] * cow[(start_idx + 2) % N] * cow[(start_idx + 3) % N]
    
    return S


N, Q = map(int, input().split())
cow = list(map(int, input().split()))
queries = list(map(int, input().split()))

# 초기 S 계산
S = initial_S(cow, N)

# 질의 처리 및 출력
for i in queries:
    idx = i - 1  # 1-based -> 0-based 인덱스
    S = update_S(cow, idx, N, S)
    print(S)