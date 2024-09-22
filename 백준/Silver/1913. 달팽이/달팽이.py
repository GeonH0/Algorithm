N = int(input())
target = int(input())

# 2차원 배열 생성
snail = [[0] * N for _ in range(N)]

# 시작 위치 (좌상단)
x, y = 0, 0
num = N * N

# 방향 (하, 우, 상, 좌)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction = 0

# 달팽이 채우기
while num > 0:
    snail[x][y] = num
    if num == target:
        target_x, target_y = x, y
    
    nx, ny = x + dx[direction], y + dy[direction]
    if 0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0:
        x, y = nx, ny
    else:
        direction = (direction + 1) % 4
        x, y = x + dx[direction], y + dy[direction]
    
    num -= 1

# 결과 출력
for row in snail:
    print(*row)

print(target_x + 1, target_y + 1)