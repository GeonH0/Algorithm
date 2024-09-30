# R,S = map(int,input().split())
# arr = []
# ans = [['']*S for _ in range(R)]
# meteor_positions = []
# for _ in range(R):
#     arr.append(list(input().rstrip()))

# # 유성의 위치를 찾는다.
# for i in range(R):
#     for j in range(S):
#         if arr[i][j] == "X":
#             meteor_positions.append((i,j))

# min_drop_distance = R

# for j in range(S):
#     cnt = -1
#     first_ground = R

#     # 해당 열의 유성의 최하단 위치와 땅 위치 찾기
#     for i in range(R):
#         if arr[i][j] == "X":
#             cnt = max(cnt,i)
#         elif arr[i][j] == "#" and cnt != -1:
#             first_ground = min(first_ground,i)
#     # 낙하 가능 거리 계산
#     if cnt != -1:
#         min_drop_distance = min(min_drop_distance,first_ground-cnt -1)

# result = [row[:] for row in arr]

# for (i,j) in meteor_positions:
#     result[i][j] = "."
#     result[i+min_drop_distance][j] = "X"
    
# for row in result:
#     print(''.join(row))        


R, S = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(input().rstrip()))

# 유성의 각 좌표 위치를 기록
meteor_positions = []

# 땅의 위치를 기록하여 유성과 땅 사이의 최소 거리를 계산
for i in range(R):
    for j in range(S):
        if arr[i][j] == "X":
            meteor_positions.append((i, j))

# 유성이 낙하할 수 있는 최대 거리 계산
min_drop_distance = R

# 각 열마다 유성의 최하단과 땅 사이의 거리 계산
for j in range(S):
    lowest_meteor = -1
    first_ground = R

    # 해당 열의 유성의 최하단 위치와 땅 위치 찾기
    for i in range(R):
        if arr[i][j] == "X":
            lowest_meteor = max(lowest_meteor, i)
        elif arr[i][j] == "#" and lowest_meteor != -1:
            first_ground = min(first_ground, i)
    
    # 낙하 가능 거리 계산
    if lowest_meteor != -1:
        min_drop_distance = min(min_drop_distance, first_ground - lowest_meteor - 1)

# 유성을 떨어뜨린 후의 배열을 초기화
result = [row[:] for row in arr]

# 유성의 위치를 낙하 거리만큼 이동
# 유성의 원래 위치를 공기('.')로 변경
for (i, j) in meteor_positions:
    result[i][j] = '.'

# 유성의 새로운 위치로 업데이트
for (i, j) in meteor_positions:
    result[i + min_drop_distance][j] = 'X'

# 결과 출력
for row in result:
    print(''.join(row))